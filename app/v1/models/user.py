from sqlalchemy import Column, TEXT, ForeignKey, String, Integer, Enum, TIMESTAMP, text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base


class User(Base):
   __tablename__ = "user"

   id = Column(Integer, primary_key=True, index=True)
   username = Column(String(255), unique=True, nullable=False, index=True)
   password = Column(String(255), nullable=False)
   email = Column(String(255), unique=True, nullable=False, index=True)
   name = Column(String(50), nullable=False, index=True)
   role_id = Column(Integer, ForeignKey('role.id'), server_default="4", index=True)

   id_type = Column(Integer, ForeignKey('user_id_type.id'), index=True)
   id_number = Column(String(50), index=True)
   phone = Column(String(15))
   address = Column(TEXT)

   status = Column(Enum('true', 'false'), nullable=False, server_default='false', index=True)
   creator = Column(Integer)
   created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
   editor = Column(Integer)
   updated_at = Column(TIMESTAMP(timezone=True), server_default=text("NULL ON UPDATE CURRENT_TIMESTAMP"))
