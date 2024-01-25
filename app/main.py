from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.v1 import router


def get_application():
   _app = FastAPI(
      title=settings.PROJECT_NAME,
      summary="A blueprint of a SIMPLE BACKEND (Simbe) with the latest version of FastAPI, Pydantic, SQLAlchemy and Alembic",
      version="v0.1.0-alpha",
      terms_of_service="https://github.com/setia1011/simbe",
      contact={
         "name": "Setiadi H.",
         "url": "https://github.com/setia1011/simbe",
         "email": "setiadi1457@gmail.com",
      }
   )

   _app.add_middleware(
      CORSMiddleware,
      allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
   )

   return _app


app = get_application()
app.include_router(router=router)