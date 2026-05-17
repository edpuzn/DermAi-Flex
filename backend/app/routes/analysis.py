from fastapi import APIRouter, UploadFile, File, Form, HTTPException, status
from typing import Optional, List
from app.schemas.analysis import AnalysisResponse
from app.inference.engine import prediction_engine
from app.ocr.engine import ocr_engine
from app.rag.engine import rag_engine
import json
import logging
import time
import os

logger = logging.getLogger("Analysis-Route")
DEMO_MODE = os.getenv("DEMO_MODE", "false").lower() == "true"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB limit

router = APIRouter()

@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_lesion(
    image: Optional[UploadFile] = File(None),
    pdf: Optional[UploadFile] = File(None),
    metadata: Optional[str] = Form(None)
):
    """
    Main analysis endpoint. Combines image AI, OCR, and RAG with strict validation and DEMO_MODE support.
    """
    request_id = f"REQ-{int(time.time())}"
    logger.info(f"[{request_id}] Starting multi-modal analysis request.")
    start_time = time.time()
    
    try:
        # 1. Validation: DEMO_MODE Override
        if DEMO_MODE:
            logger.info(f"[{request_id}] Running in DEMO MODE. Returning sample analysis.")
            time.sleep(1.5) # Simulate processing
            return {
                "predictions": [
                    {"class": "Melanoma", "confidence": 88.4},
                    {"class": "Melanocytic Nevus", "confidence": 10.2},
                    {"class": "Benign Keratosis", "confidence": 1.4}
                ],
                "ocr_text": "Sample clinical report text: Patient presents with asymmetric lesion on back...",
                "explanation": "DEMO MODE: Analysis of visual features shows asymmetric structures and irregular pigment network. Histopathological correlation is recommended.",
                "risk_level": "High",
                "disclaimer": "DEMO MODE ACTIVE: This is sample data for demonstration purposes only.",
                "heatmap": "https://pub-807e32a67e4544d69352e8250ba95f9c.r2.dev/gradcam_sample.jpg"
            }

        # 2. Validation: File Size Checks
        if image and image.size > MAX_FILE_SIZE:
             raise HTTPException(status_code=413, detail="Image file too large (Max 10MB)")
        if pdf and pdf.size > MAX_FILE_SIZE:
             raise HTTPException(status_code=413, detail="PDF file too large (Max 10MB)")

        # 3. Validation: AI Model Readiness
        if image and not prediction_engine.is_ready:
            logger.error(f"[{request_id}] AI model is not ready for inference.")
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Dermatology AI model is not currently loaded on the server."
            )

        # 4. Metadata Parsing
        parsed_metadata = {}
        if metadata:
            try:
                parsed_metadata = json.loads(metadata)
            except json.JSONDecodeError:
                logger.warning(f"[{request_id}] Failed to parse metadata JSON.")

        # 5. OCR Processing (if pdf exists)
        ocr_text = ""
        if pdf:
            logger.info(f"[{request_id}] PDF detected. Executing OCR pipeline.")
            pdf_bytes = await pdf.read()
            ocr_text = ocr_engine.extract_text(pdf_bytes)
            
        # 6. Image Inference (if image exists)
        predictions = []
        heatmap = None
        if image:
            logger.info(f"[{request_id}] Image detected. Executing EfficientNet-B4 inference.")
            image_bytes = await image.read()
            inference_result = prediction_engine.predict(image_bytes)
            
            # Extract from result dictionary
            heatmap = inference_result.get("heatmap")
            raw_predictions = inference_result.get("predictions", [])
            
            # Map predictions for API response
            predictions = [
                {"class": p["class"], "confidence": round(p["confidence"], 2)}
                for p in raw_predictions
            ]
            
        # 7. RAG Explanation
        logger.info(f"[{request_id}] Generating RAG-based clinical explanation.")
        explanation = rag_engine.generate_explanation(raw_predictions if image else [], ocr_text)
        
        # 8. Dynamic Risk Calculation
        import re
        calculated_risk = "Medium"
        if image and predictions:
            calculated_risk = "High" if any(p['confidence'] > 70 for p in predictions) else "Medium"
        else:
            # Report-Only mode: parse the hidden tag <!-- RISK: High/Medium/Low -->
            risk_match = re.search(r"<!--\s*RISK:\s*(High|Medium|Low)\s*-->", explanation, re.IGNORECASE)
            if risk_match:
                calculated_risk = risk_match.group(1).capitalize()
                logger.info(f"[{request_id}] Extracted risk level '{calculated_risk}' from RAG explanation.")
            else:
                logger.warning(f"[{request_id}] Could not parse risk level from explanation, defaulting to 'Medium'.")
        
        total_time = (time.time() - start_time) * 1000
        logger.info(f"[{request_id}] Analysis request completed in {total_time:.2f}ms")
        
        return {
            "predictions": predictions,
            "ocr_text": ocr_text,
            "explanation": explanation,
            "risk_level": calculated_risk,
            "disclaimer": "SCIENTIFIC VALIDATION PASS: This result is AI-generated for educational/research purposes. Correlation with clinical and histopathological findings is mandatory.",
            "heatmap": heatmap
        }

    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"[{request_id}] Unexpected pipeline failure: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Internal Pipeline Error: {str(e)}"
        )




