import os
import paddle
from paddleocr import PaddleOCR
import numpy as np
from PIL import Image
import io
import logging
import time

logger = logging.getLogger("OCR-Pipeline")

class OCREngine:
    def __init__(self):
        try:
            # Fully compatible flags for PaddleOCR 2.7.3
            self.ocr = PaddleOCR(
                use_angle_cls=True, 
                lang='en', 
                use_gpu=False, 
                show_log=False
            ) 
            logger.info("✅ OCR Engine initialized with PaddleOCR.")
        except Exception as e:
            logger.error(f"❌ Failed to initialize OCR Engine: {e}")
            raise e

    def _clean_pii(self, text):
        """
        Kişisel verileri (İsim, T.C., Tarih vb.) metinden temizler.
        """
        import re
        # Filtreleme desenleri
        patterns = [
            r"Adı\s*[:\/]\s*[A-ZÇĞİÖŞÜa-zçğıöşü\s]+", # İsim
            r"Soyadı\s*[:\/]\s*[A-ZÇĞİÖŞÜa-zçğıöşü\s]+", # Soyisim
            r"TC\s*Kimlik\s*No\s*[:\/]\s*\d+", # TC No
            r"Doğum\s*Tarihi\s*[:\/]\s*[\d\.]+", # Doğum Tarihi
            r"Cinsiyet\s*[:\/]\s*[A-ZÇĞİÖŞÜa-zçğıöşü]+", # Cinsiyet
            r"\b\d{11}\b", # Herhangi bir 11 haneli sayı (TC olabilir)
        ]
        
        cleaned = text
        for pattern in patterns:
            cleaned = re.sub(pattern, "[GİZLİ VERİ]", cleaned, flags=re.IGNORECASE)
        
        return cleaned

    def extract_text(self, file_bytes):
        if not self.ocr:
            return ""

        full_text = ""
        try:
            # Check if it's a PDF
            if file_bytes.startswith(b"%PDF"):
                logger.info("Processing PDF document via OCR...")
                import fitz
                doc = fitz.open(stream=file_bytes, filetype="pdf")
                for page in doc:
                    pix = page.get_pixmap()
                    img_bytes = pix.tobytes("png")
                    img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
                    img_np = np.array(img)
                    
                    result = self.ocr.ocr(img_np)
                    if result:
                        for idx in range(len(result)):
                            res = result[idx]
                            if res:
                                for line in res:
                                    full_text += line[1][0] + " "
            else:
                # Process as Image
                logger.info("Processing image via OCR...")
                img = Image.open(io.BytesIO(file_bytes)).convert('RGB')
                img_np = np.array(img)
                result = self.ocr.ocr(img_np)
                if result:
                    for idx in range(len(result)):
                        res = result[idx]
                        if res:
                            for line in res:
                                full_text += line[1][0] + " "
            return full_text
        except Exception as e:
            logger.error(f"OCR processing failed: {e}")
            raise RuntimeError(f"OCR Pipeline Error: {str(e)}")

    def clean_text(self, text):
        if not text:
            return ""
        import re
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

ocr_engine = OCREngine()

