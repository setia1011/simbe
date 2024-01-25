import datetime
import math
from typing import Union
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import db_sync_session
from app.v1.models.user import User
from app.v1.schemas import err as sc_err
from app.v1.schemas import user as sc_user
from app.v1.services import user as sv_user


router = APIRouter()


@router.get('/users', name="Get all users", response_model=list[sc_user.User])
def users(db: Session = Depends(db_sync_session)):
   return sv_user.get_user_all(db=db)

@router.post("/user", name="Create a new user", response_model=sc_user.User)
def user(t: sc_user.UserPost, db: Session = Depends(db_sync_session)):
   return sv_user.user_post(t=t, db=db)

@router.patch("/user", name="Update a user", response_model=sc_user.User)
def user(t: sc_user.UserPost, db: Session = Depends(db_sync_session)):
   return sv_user.user_patch(t=t, db=db)

@router.post("/user/role", name="Create a new user role", response_model=sc_user.Role)
def role(t: sc_user.RolePost, db: Session = Depends(db_sync_session)):
   return sv_user.role_post(t=t, db=db)

# with error handling try except raise
@router.post("/user/id-type", name="Create a new user ID type", response_model=sc_user.IdType)
def id_type(t: sc_user.IdTypePost, db: Session = Depends(db_sync_session)):
   try:
      return sv_user.id_type_post(t=t, db=db)
   except:
      raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Failed')