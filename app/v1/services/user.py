import datetime
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select, insert, desc, func, delete
from app.v1.models import User


def get_user_all(db: Session = Depends):
   return db.execute(select(User)).scalars().all()
