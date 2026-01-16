from fastapi import FastAPI
from src.app.api.v1 import router as v1_router

app = FastAPI(title="AI Detector API")


@app.get("/health")
def healthcheck():
    return {"status": "ok"}

app.include_router(v1_router, prefix="/api/v1")
