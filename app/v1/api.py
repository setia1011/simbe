from fastapi import APIRouter
from app.v1.routers import home

router_v1 = APIRouter()
router_v1.include_router(home.router, prefix='', tags=['home'])