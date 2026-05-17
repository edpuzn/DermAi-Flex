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
            try:
                genai.configure(api_key=api_key)
                
                # Profesyonel Sistem Talimatı (System Instruction)
                system_instruction = """
                Sen DermAI-Flex platformunun Klinik Karar Destek Asistanısın (CDSS). 
                Görevin, verileri sentezleyerek temiz HTML formatında bir rapor sunmaktır.
                
                FORMAT KURALLARI:
                1. ASLA Markdown karakterleri (####, **, ---) kullanma.
                2. Yanıtını sadece HTML etiketleri (<h3>, <p>, <ul>, <li>, <strong>) kullanarak yapılandır.
                3. Profesyonel ve temiz bir görünüm için paragrafları <p> içinde sun.
                4. Her zaman Türkçe ve profesyonel bir dil kullan.
                5. Başlıklarda (<h3>) kesinlikle emoji KULLANMA.
                """
                
                self.model = genai.GenerativeModel(
                    model_name='gemini-2.5-flash', 
                    system_instruction=system_instruction
                )
                
                # Log key status (masked)
                masked_key = f"{api_key[:4]}...{api_key[-4:]}" if len(api_key) > 8 else "***"
                logger.info(f"🔑 Gemini API Key found: {masked_key}")
                logger.info("✅ Gemini Decision Support System (CDSS) initialized.")
            except Exception as e:
                self.model = None
                logger.error(f"❌ Gemini Configuration Error: {e}")
        else:
            self.model = None
            logger.warning("⚠️ GEMINI_API_KEY not found in environment! Check your .env file.")

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

    def _generate_report_only_explanation(self, ocr_text):
        if not self.model:
            return "Gemini API aktif değil."
            
        prompt = f"""
        Aşağıda, bir hastaya ait laboratuvar tahlili veya patoloji raporundan elde edilen OCR metin verileri verilmiştir.
        Bu tıbbi verileri analiz ederek temiz HTML formatında bir 'Klinik Karar Destek Raporu' oluştur.
        Markdown karakterlerini (**, #, -) kesinlikle KULLANMA.
        
        OCR METİN VERİLERİ:
        {ocr_text}
        
        YAPMAN GEREKENLER:
        1. Metin içindeki tüm anormal/sınır dışı tıbbi değerleri (örneğin WBC, CRP, Vitamin D vb.) tespit et ve 'Analiz Özeti' bölümünde açıkla.
        2. Bu değerlerin klinik korelasyonunu ve olası klinik anlamlarını (örneğin yüksek CRP ve WBC'nin aktif enfeksiyona işaret etmesi vb.) 'Klinik Korelasyon' bölümünde yorumla.
        3. Hekime kılavuzluk edecek 'Önerilen Sonraki Adımlar' (örneğin uzman dermatolog konsültasyonu, ileri tetkik, rutin takip vb.) sun.
        4. Analiz ettiğin verilere dayanarak hastanın genel risk seviyesini 'High', 'Medium' veya 'Low' olarak belirle ve bunu HTML'in en sonuna gizli bir yorum satırı olarak ekle: <!-- RISK: RiskSeviyesi --> (Örn: <!-- RISK: High -->)
        
        İSTENEN HTML YAPISI ÖRNEĞİ:
        <h3>Analiz Özeti</h3>
        <p>...</p>
        <h3>Klinik Korelasyon</h3>
        <ul><li>...</li></ul>
        <h3>Önerilen Sonraki Adımlar</h3>
        <p>...</p>
        <hr>
        <p><strong>Uyarı:</strong> Bu bir tıbbi teşhis değildir. Sadece klinik karar destek amaçlıdır.</p>
        <!-- RISK: High -->
        """
        
        try:
            response = self.model.generate_content(prompt)
            clean_html = response.text.replace('```html', '').replace('```', '').strip()
            return clean_html
        except Exception as e:
            logger.error(f"Gemini API Report-Only Error: {e}")
            return "Gemini sentezleme hatası. Lütfen daha sonra tekrar deneyin."

    def generate_explanation(self, predictions, ocr_text):
        if not predictions:
            if ocr_text:
                return self._generate_report_only_explanation(ocr_text)
            return "Analiz verisi yetersiz."

        top_pred = predictions[0]
        # PredictionEngine now uses 'class' instead of 'label'
        class_name = top_pred['class']
        confidence = top_pred['confidence'] # Already multiplied by 100 in engine.py
        
        # 1. Kan Değerlerini Ayıkla
        blood_data = self._analyze_blood_work(ocr_text) if ocr_text else {}

        # 2. Literatürden Bilgi Çek (RAG)
        context_data = self.collection.query(query_texts=[class_name], n_results=2)
        retrieved_docs = context_data.get('documents', [[]])[0]
        
        # 3. Gemini ile Akıllı Sentez
        if self.model:
            prompt = f"""
            Aşağıdaki verileri sentezleyerek temiz HTML formatında bir 'Klinik Karar Destek Raporu' oluştur.
            Markdown karakterlerini (**, #, -) kesinlikle KULLANMA.

            [VERİLER]
            - Tahmin: {class_name} (Güven: %{confidence:.1f})
            - Kan Değerleri: {blood_data}
            - Referanslar: {retrieved_docs}

            İSTENEN HTML YAPISI ÖRNEĞİ:
            <h3>Analiz Özeti</h3>
            <p>...</p>
            <h3>Klinik Korelasyon</h3>
            <ul><li>...</li></ul>
            <h3>Önerilen Sonraki Adımlar</h3>
            <p>...</p>
            <hr>
            <p><strong>Uyarı:</strong> Bu bir tıbbi teşhis değildir...</p>
            """
            
            try:
                response = self.model.generate_content(prompt)
                # Ensure no markdown backticks wrap the HTML
                clean_html = response.text.replace('```html', '').replace('```', '').strip()
                return clean_html
            except Exception as e:
                logger.error(f"Gemini API Error: {e}")
                return "Gemini sentezleme hatası. Lütfen daha sonra tekrar deneyin."
        
        # Fallback (API yoksa eski yöntem)
        return f"Gemini API aktif değil. Görsel tahmin: {class_name} (%{confidence:.1f})"

rag_engine = RAGEngine()
