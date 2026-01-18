from fastapi import APIRouter
from .endpoints import auth, health, root

router = APIRouter()

# Подключаем endpoints
router.include_router(auth.router)
router.include_router(health.router)
router.include_router(root.router)
