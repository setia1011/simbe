from fastapi import APIRouter
from app.v1.routers import home, user

router_v1 = APIRouter()
router_v1.include_router(home.router, prefix='', tags=['home'])
router_v1.include_router(user.router, prefix='/v1/api', tags=['user'])