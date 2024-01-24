from fastapi import APIRouter
from directory_tree import display_tree

router = APIRouter()

@router.get("/", description="Home")
def home():
   return {"detail": "Welcome to Simbe"}

@router.get("/tree", description="Tree")
def home():
   return display_tree(header=True, max_depth=3)