from fastapi import APIRouter, HTTPException, status
from app.schemas.auth import LoginRequest, AuthResponse

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login", response_model=AuthResponse)
async def login(data: LoginRequest):
    # Тестовая логика авторизации
    if data.email == "user@example.com" and data.password == "123456":
        return {"access_token": "fake_token_for_now", "token_type": "bearer"}
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Неверный email или пароль"
    )

