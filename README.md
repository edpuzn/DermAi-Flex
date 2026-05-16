# DermAI-Flex: Multi-Modal Dermatology Assistant

DermAI-Flex is an AI-powered dermatological analysis platform that fusions visual lesion imagery with clinical reports (PDF) using state-of-the-art Deep Learning (EfficientNet-B4), OCR (PaddleOCR), and Multi-RAG (ChromaDB).

## 🚀 Quick Start (Docker)

To run the entire platform with a single command:

1. **Place Model**: Ensure `backend/outputs/best_phase2.pth` is present.
2. **Run Compose**:
   ```bash
   docker compose up --build
   ```
3. **Access**:
   - **Frontend**: [http://localhost:5173](http://localhost:5173)
   - **Backend Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

For detailed Docker instructions, see [DOCKER_GUIDE.md](DOCKER_GUIDE.md).

## 🛠️ Local Development

### Backend
1. `cd backend`
2. `pip install -r requirements.txt`
3. `python -m uvicorn app.main:app --reload`

### Frontend
1. `cd frontend`
2. `npm install`
3. `npm run dev`

For testing and validation details, see [TESTING_CHECKLIST.md](TESTING_CHECKLIST.md) and [AI_VALIDATION_REPORT.md](AI_VALIDATION_REPORT.md).

---
*Graduation Project - 2026*
