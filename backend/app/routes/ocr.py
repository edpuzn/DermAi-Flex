from fastapi import APIRouter, UploadFile, File, HTTPException
from app.ocr.engine import ocr_engine

router = APIRouter()

@router.post("/process")
async def process_ocr(file: UploadFile = File(...)):
    try:
        content = await file.read()
        text = ocr_engine.extract_text(content)
        cleaned_text = ocr_engine.clean_text(text)
        return {"text": cleaned_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OCR processing failed: {str(e)}")
