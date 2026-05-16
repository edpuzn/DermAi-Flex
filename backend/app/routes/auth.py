from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    username: str

@router.post("/login", response_model=LoginResponse)
async def login(data: LoginRequest):
    # Simple hardcoded credentials for demo stability
    if data.username == "admin" and data.password == "admin123":
        return {
            "access_token": "demo_token_123",
            "token_type": "bearer",
            "username": "admin"
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Geçersiz kullanıcı adı veya şifre"
        )
