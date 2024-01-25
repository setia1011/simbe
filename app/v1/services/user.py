import datetime
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select, insert, desc, func, delete
from app.v1.models import User, Role, IdType
from app.v1.schemas import user as sc_user


def get_user_all(db: Session = Depends):
   return db.execute(select(User)).scalars().all()

def get_user_by_username(username: str, db: Session = Depends):
   return db.execute(select(User).filter(User.username==username)).scalar_one_or_none()

def user_patch(t: sc_user.UserPost, db: Session = Depends):
   user = get_user_by_username(username=t.username, db=db)
   if user is None:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User not found')
   # insert editor, you can get editor from session
   user.editor = 1
   for key, value in t.model_dump(exclude_unset=True, exclude_none=True).items():
      setattr(user, key, value)
   return user

def user_post(t: sc_user.UserPost, db: Session = Depends):
   a = db.execute(insert(User).values(username=t.username, password=t.password, name=t.name, email=t.email, role_id=t.role_id, id_type_id=t.id_type_id, id_number=t.id_number, phone=t.phone, address=t.address))
   b = db.execute(select(User).filter(User.id==a.lastrowid)).scalar_one_or_none()
   return b

def role_post(t: sc_user.RolePost, db: Session = Depends):
   a = db.execute(insert(Role).values(role=t.role, role_description=t.role_description))
   b = db.execute(select(Role).filter(Role.id==a.lastrowid)).scalar_one_or_none()
   return b

def id_type_post(t: sc_user.IdTypePost, db: Session = Depends):
   a = db.execute(insert(IdType).values(id_type=t.id_type, id_description=t.id_description))
   b = db.execute(select(IdType).filter(IdType.id==a.lastrowid)).scalar_one_or_none()
   return b
