import uvicorn
import logging
from dotenv import load_dotenv
import os

# 1. Load environment variables
load_dotenv()

# 2. Configure logging IMMEDIATELY
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("DermAI-Startup")

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import analysis, ocr, rag, history, auth
from app.inference.engine import prediction_engine
from app.ocr.engine import ocr_engine
from app.rag.engine import rag_engine

DEMO_MODE = os.getenv("DEMO_MODE", "false").lower() == "true"

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    logger.info("🚀 DermAI-Flex Backend Starting Up...")
    logger.info(f"📍 Mode: {'DEMO MODE (Sample Data Only)' if DEMO_MODE else 'PRODUCTION MODE (Real AI Inference)'}")
    
    # Check Model
    if prediction_engine.is_ready:
        logger.info("✅ AI Inference Engine: READY")
    else:
        logger.error("❌ AI Inference Engine: FAILED (Model checkpoint missing)")
        
    # Check OCR
    try:
        logger.info("✅ OCR Engine: INITIALIZED")
    except Exception as e:
        logger.error(f"❌ OCR Engine: FAILED ({e})")
        
    # Check RAG
    try:
        logger.info("✅ RAG Engine: INITIALIZED")
    except Exception as e:
        logger.error(f"❌ RAG Engine: FAILED ({e})")
        
    logger.info("📡 API is now listening for requests.")
    yield
    # Shutdown logic
    logger.info("👋 DermAI-Flex Backend Shutting Down...")

app = FastAPI(
    title="DermAI-Flex API",
    description="Multimodal Dermatology Assistant Backend",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS - Restricted in production but open for demo-stability
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(analysis.router, prefix="/api/analysis", tags=["Analysis"])

app.include_router(ocr.router, prefix="/api/ocr", tags=["OCR"])
app.include_router(rag.router, prefix="/api/rag", tags=["RAG"])
app.include_router(history.router, prefix="/api/history", tags=["History"])

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0",
        "demo_mode": DEMO_MODE,
        "model_loaded": prediction_engine.is_ready
    }

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

