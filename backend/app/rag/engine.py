import chromadb
from chromadb.utils import embedding_functions
import os
import logging
import time
import re
import google.generativeai as genai

logger = logging.getLogger("RAG-Pipeline")

class RAGEngine:
    def __init__(self, db_path="app/vector_db/chroma"):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        # Gemini Setup
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
            logger.info("✅ Gemini 1.5 Flash Engine initialized.")
        else:
            self.model = None
            logger.warning("⚠️ GEMINI_API_KEY not found. Falling back to local synthesis.")

        try:
            self.client = chromadb.PersistentClient(path=db_path)
            self.embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
                model_name="BAAI/bge-small-en-v1.5"
            )

            self.collection = self.client.get_or_create_collection(
                name="medical_docs",
                embedding_function=self.embedding_func
            )
            logger.info("✅ RAG Engine initialized with ChromaDB.")
        except Exception as e:
            logger.error(f"❌ Failed to initialize RAG Engine: {e}")
            raise e

    def _analyze_blood_work(self, text):
        """
        Metin içindeki kan değerlerini saptar (Rule-based pre-processing).
        """
        interpretations = []
        text_lower = text.lower()
        
        # Vitamin D, CRP, WBC taraması
        metrics = {
            "Vitamin D": r"(vitamin\s*d|vit\s*d|25-oh)\s*[:\/]?\s*(\d+[\.,]?\d*)",
            "CRP": r"(crp|c-reaktif)\s*[:\/]?\s*(\d+[\.,]?\d*)",
            "WBC": r"(wbc|akyuvar)\s*[:\/]?\s*(\d+[\.,]?\d*)"
        }
        
        found_data = {}
        for name, pattern in metrics.items():
            match = re.search(pattern, text_lower)
            if match:
                val = float(match.group(2).replace(',', '.'))
                found_data[name] = val
        
        return found_data

    def generate_explanation(self, predictions, ocr_text):
        if not predictions:
            return "Analiz verisi yetersiz."

        top_pred = predictions[0]
        label = top_pred['label']
        confidence = top_pred['confidence']
        
        # 1. Kan Değerlerini Ayıkla
        blood_data = self._analyze_blood_work(ocr_text) if ocr_text else {}

        # 2. Literatürden Bilgi Çek (RAG)
        context_data = self.collection.query(query_texts=[label], n_results=2)
        retrieved_docs = context_data.get('documents', [[]])[0]
        
        # 3. Gemini ile Akıllı Sentez
        if self.model:
            prompt = f"""
            Sen profesyonel, şefkatli ve uzman bir dermatoloji asistanısın. Görevin, bir hastaya yapay zeka analiz sonuçlarını anlaşılır ve uygulanabilir bir dille açıklamak.
            
            VERİLER:
            - Görsel Analiz Tahmini: {label} (Güven Oranı: %{confidence*100:.1f})
            - Kan Değerleri (OCR): {blood_data}
            - Tıbbi Literatür Notları: {retrieved_docs}
            - Ham OCR Metni (Filtrelenmiş): {ocr_text[:500] if ocr_text else 'Yok'}

            TALİMATLAR:
            1. Teknik terimleri açıkla (örneğin Aktinik Keratoz ne demek?).
            2. Kan değerleri ile cilt durumunu ilişkilendir (Örn: D vitamini düşükse bunun cilt sağlığına etkisini söyle).
            3. Hastaya panik yaptırmadan, somut 'Sonraki Adımlar' öner.
            4. Dili her zaman Türkçe olsun.
            5. Cevabın sonunda mutlaka 'Bu bir tıbbi teşhis değildir, mutlaka doktorunuza danışın' uyarısını ekle.
            6. Yanıtını Markdown formatında (başlıklar, listeler kullanarak) düzenle.
            """
            
            try:
                response = self.model.generate_content(prompt)
                return response.text
            except Exception as e:
                logger.error(f"Gemini API Error: {e}")
                return "Gemini sentezleme hatası. Lütfen daha sonra tekrar deneyin."
        
        # Fallback (API yoksa eski yöntem)
        return f"Gemini API aktif değil. Görsel tahmin: {label} (%{confidence*100:.1f})"

rag_engine = RAGEngine()
