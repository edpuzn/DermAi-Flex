# 🏥 DermAI-Flex: Final System Status & Presentation Guide

## 1. System Components & Startup Order
The system is architected for high availability during a live presentation.

1.  **Backend (FastAPI)**: Initializes AI model, OCR engines, and ChromaDB.
    - *Startup Time*: ~15-40 seconds (depending on hardware and model loading).
    - *Health Check*: Available at `/health` once fully ready.
2.  **Frontend (Vue 3)**: Waits for the Backend health check to pass before becoming operational in the browser.

## 2. Docker Service Map
| Service | Image | Internal Port | External Port | Role |
|---------|-------|---------------|---------------|------|
| `backend` | `python:3.10-slim` | 8000 | 8000 | AI Inference, OCR, RAG Engine |
| `frontend` | `node:18-alpine` | 5173 | 5173 | Dashboard & Visualization |

## 3. Runtime Reliability Features
- **Fail-Safe Inference**: If the model checkpoint (`best_phase2.pth`) is missing, the backend returns a `503 Service Unavailable` error, and the UI displays a clean error message instead of crashing or returning fake data.
- **DEMO_MODE Support**: Set `DEMO_MODE=true` in `docker-compose.yml` to run the system with pre-defined sample data—ideal for environments with low RAM or missing GPU drivers.
- **Persistence**: ChromaDB vector storage is mounted to `./backend/app/vector_db`, ensuring medical context persists across restarts.
- **Robust OCR**: System dependencies (`libgl1`, `libsm6`, etc.) are pre-configured in the Dockerfile to ensure PaddleOCR works in any container environment.

## 4. Presentation Checklist
- [ ] Docker Desktop/Engine is running.
- [ ] Port 8000 and 5173 are free.
- [ ] `backend/outputs/best_phase2.pth` is present (for real inference).
- [ ] Run `docker compose up --build`.
- [ ] Open `http://localhost:5173`.
- [ ] Verify "ONLINE" status and "DEMO MODE" label in header (if enabled).

## 5. Technical Specs
- **Expected RAM Usage**: 
  - Backend: 1.5GB - 3GB (Model weights + OCR + ChromaDB).
  - Frontend: 150MB.
- **Max Upload Size**: 10MB (enforced via backend).
- **Request Timeout**: 60 seconds (enforced via frontend).

## 6. Known Runtime Risks
- **Cold Start**: The first OCR request may take longer as PaddleOCR downloads language models.
- **CPU Inference**: On machines without NVIDIA GPUs, inference timing will increase to 2-5 seconds per image.

---
**Status**: 🟢 **STABLE & PRODUCTION-READY**
*Validated for Windows (WSL2), Linux, and macOS.*
