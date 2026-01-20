# src/app/api/v1/endpoints/auth.py
from fastapi import APIRouter, HTTPException, status
from app.schemas.auth import LoginRequest, AuthResponse

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

# Заглушка для проверки POST
@router.post("/login", response_model=AuthResponse)
async def login(data: LoginRequest):
    # Временная логика: проверка email и password
    if data.email == "test@example.com" and data.password == "123456":
        return {"access_token": "fake_token_for_now", "token_type": "bearer"}
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Неверный email или пароль"
    )
