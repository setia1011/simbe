import datetime
import math
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import db_sync_session
from app.v1.models.user import User
from app.v1.schemas import user as sc_user
from app.v1.services import user as sv_user


router = APIRouter()


@router.get('/users', response_model=list[sc_user.User])
def users(db: Session = Depends(db_sync_session)):
   return sv_user.get_user_all(db=db)