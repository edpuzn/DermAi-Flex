# 🧪 DermAI-Flex Testing Checklist

This document provides instructions for running and verifying the DermAI-Flex system end-to-end.

## 🏗️ Environment Setup

### 1. Backend Setup
- **Directory**: `backend/`
- **Requirements**: `pip install -r requirements.txt`
- **Model Checkpoint**: Ensure `best_phase2.pth` is located at `backend/outputs/best_phase2.pth`.
- **Command**: 
  ```bash
  cd backend
  python -m uvicorn app.main:app --reload
  ```
- **Verification**: Open `http://127.0.0.1:8000/health` in your browser. You should see `{"status": "healthy", "version": "1.0.0"}`.

### 2. Frontend Setup
- **Directory**: `frontend/`
- **Install**: `npm install`
- **Command**: `npm run dev`
- **Base URL**: The frontend is configured to talk to `http://127.0.0.1:8000/api`. Ensure the backend is running.

---

## 🔍 Testing Pipeline

### 🟢 Phase 1: Health Checks
- [ ] Backend starts without errors (`✅ Model loaded successfully` should appear in logs).
- [ ] Frontend starts and displays the Landing Page.
- [ ] `/health` endpoint returns success.

### 🟡 Phase 2: Image Analysis
- [ ] Navigate to the Dashboard.
- [ ] Upload a dermatological image (JPG/PNG).
- [ ] Click "Run Analysis".
- [ ] **Expectation**: Loading spinner appears, then redirects to Result Page.
- [ ] **Verification**: Result Page shows the uploaded image and Top-3 predictions with percentages.

### 🔵 Phase 3: OCR & RAG
- [ ] Upload a PDF clinical report.
- [ ] Click "Run Analysis".
- [ ] **Verification**: Result Page displays extracted text in the "Extracted Medical Data (OCR)" section.
- [ ] **Verification**: AI Explanation section displays synthesized reasoning.

---

## 🛠️ Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `Model checkpoint not found` | File missing in `outputs/` | Place `best_phase2.pth` in `backend/outputs/`. |
| `CORS Error` | Backend not allowing origins | Check `CORSMiddleware` in `app/main.py`. It is currently set to `*`. |
| `OCR failed` | Missing Paddle dependencies | Ensure `paddlepaddle` and `paddleocr` are installed. On Windows, you may need `msvc-runtime`. |
| `ECONNREFUSED` | Backend not running | Start the FastAPI server on port 8000. |

## 📐 Model Specifications
- **Architecture**: EfficientNet-B4
- **Input Size**: 380x380 (Center Crop)
- **Normalization**: ImageNet Mean/Std
- **Output**: 7 Classes (Standard ISIC Order: AK, BCC, BKL, DF, MEL, NV, VASC)

## 📊 Logging & Verification
- Check backend console for:
  - `✅ Model loaded successfully`
  - `Inference completed in XXXms`
  - `RAG query completed in XXXms`
  - `OCR execution completed in XXXms`

