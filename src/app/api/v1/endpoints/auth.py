from fastapi import APIRouter
from app.schemas.auth import LoginRequest, RegisterRequest, AuthResponse

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=AuthResponse)
async def login(request: LoginRequest):
    # пока просто возвращаем тестовые данные
    return AuthResponse(access_token="testtoken123")

@router.post("/register", response_model=AuthResponse)
async def register(request: RegisterRequest):
    # пока просто возвращаем тестовые данные
    return AuthResponse(access_token="newusertoken123")
