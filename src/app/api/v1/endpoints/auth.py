from fastapi import APIRouter
from app.schemas.auth import LoginRequest

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login")
async def login(data: LoginRequest):
    return {
        "access_token": "fake_token_for_now",
        "token_type": "bearer"
    }

