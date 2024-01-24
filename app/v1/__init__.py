from fastapi import APIRouter
from app.v1.routers import home, user

router = APIRouter()
router.include_router(home.router, prefix='', tags=['home'])
router.include_router(user.router, prefix='/v1/api', tags=['user'])