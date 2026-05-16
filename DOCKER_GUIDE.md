# 🐳 DermAI-Flex Docker Deployment Guide

This guide explains how to build and run the DermAI-Flex platform using Docker and Docker Compose.

## 🏗️ Project Structure
```text
DermAI-Flex-main/
├── backend/
│   ├── Dockerfile
│   └── outputs/
│       └── best_phase2.pth  <-- Place model here
├── frontend/
│   ├── Dockerfile
│   └── .env.example
└── docker-compose.yml
```

## 🚀 Quick Start

### 1. Place the AI Model
Before building, ensure the EfficientNet-B4 checkpoint is in the correct location:
- **Path**: `backend/outputs/best_phase2.pth`

### 2. Build and Run
Execute the following command in the project root:
```bash
docker compose up --build
```

### 3. Access the Platform
- **Frontend**: [http://localhost:5173](http://localhost:5173)
- **Backend Health**: [http://localhost:8000/health](http://localhost:8000/health)
- **API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔍 Verification Steps

1. **Check Backend Logs**: Ensure you see `✅ Model loaded successfully`.
2. **Test Health Check**: `curl http://localhost:8000/health` should return `healthy`.
3. **Run Analysis**: Upload an image via the frontend and verify real predictions are returned from the Dockerized backend.

## 🛠️ Troubleshooting

### Model Loading Fails
- **Error**: `❌ Critical error loading model` or `503 Service Unavailable`.
- **Fix**: Ensure `best_phase2.pth` exists in `backend/outputs/`. Check the volume mount in `docker-compose.yml`.

### Port Conflicts
- **Error**: `Bind for 0.0.0.0:8000 failed: port is already allocated`.
- **Fix**: Stop any local instances of Uvicorn or other services running on port 8000 or 5173.

### Frontend API Connection
- **Issue**: Analysis fails with `Network Error`.
- **Reason**: The browser runs on your host machine, so it must use `http://127.0.0.1:8000` to reach the backend mapped from the container.

---
*DermAI-Flex Graduation Project - 2026*
