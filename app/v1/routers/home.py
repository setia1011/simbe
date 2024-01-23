from fastapi import APIRouter

router = APIRouter()

@router.get("/", description="Home")
def home():
   return {"detail": "Welcome to Simbe"}