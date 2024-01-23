from app.core.database import Base
from sqlalchemy import Column, ForeignKey, Integer, VARCHAR, TIMESTAMP, text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Role(Base):
   __tablename__ = "role"

   id = Column(Integer, primary_key=True, index=True)
   role = Column(VARCHAR(150), index=True)
   role_description = Column(VARCHAR(500), index=True)