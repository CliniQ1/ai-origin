# src/app/api/v1/router.py
from fastapi import APIRouter
from .endpoints import auth, health

router = APIRouter()

# Подключаем эндпоинты
router.include_router(auth.router)
router.include_router(health.router)
