from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login():
    return {"detail": "Not implemented yet"}

@router.post("/register")
def register():
    return {"detail": "Not implemented yet"}
