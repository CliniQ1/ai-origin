from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1",
    tags=["v1"],
)

@router.get("/health")
async def v1_health():
    return {"status": "ok"}
