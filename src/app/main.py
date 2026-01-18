from fastapi import FastAPI

from src.app.api.v1.router import router as v1_router

app = FastAPI(title="AI Origin API")

@app.get("/health")
async def health():
    return {"status": "ok"}

app.include_router(v1_router)
