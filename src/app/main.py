from fastapi import FastAPI
from app.api.v1.router import router as v1_router

app = FastAPI()

@app.get("/health")
def root_health():
    return {"status": "ok"}

app.include_router(v1_router)
