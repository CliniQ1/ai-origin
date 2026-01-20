from fastapi import FastAPI
from app.api.v1.endpoints.router import router as v1_router

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

app.include_router(v1_router, prefix="/api/v1")
