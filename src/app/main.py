# src/app/main.py
from fastapi import FastAPI
from app.api.v1 import router as v1_router

app = FastAPI()

# Healthcheck (корневой /health)
@app.get("/health")
async def health():
    return {"status": "ok"}

# Подключаем v1 router
app.include_router(v1_router, prefix="/api/v1")
