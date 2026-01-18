from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Root"])
def api_root():
    return {
        "service": "ai-origin",
        "version": "v1",
        "status": "running"
    }
