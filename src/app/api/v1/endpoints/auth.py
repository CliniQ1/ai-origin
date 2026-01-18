from fastapi import APIRouter
from app.schemas.auth import AuthLogin

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login")
async def login(data: AuthLogin):
    # тут логика авторизации
    return {"access_token": "fake_token_for_now"}

