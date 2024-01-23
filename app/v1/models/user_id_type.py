from sqlalchemy import Column, String, Integer
from app.core.database import Base


class UserIdType(Base):
   __tablename__ = "user_id_type"

   id = Column(Integer, primary_key=True, index=True)
   id_type = Column(String(50), unique=True, nullable=False, index=True)
   id_description = Column(String(225))