from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from app.core.config import settings

async_engine = AsyncEngine(create_engine(settings.DATABASE_URIX, echo=True, future=True))
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

sync_engine = create_engine(settings.DATABASE_URI, pool_pre_ping=True)
sync_session = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)

# Asynchronous database session
async def db_async_session() -> AsyncSession:
   async with async_session() as session:
      yield session

# Synchronous database session
def db_sync_session():
   db = sync_session()
   try:
      yield db
   finally:
      db.close()

@as_declarative()
class Base:

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
