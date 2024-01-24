import datetime
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional, List, Dict, Union


class MyBaseModel(BaseModel):
   class Config:
      model_config = ConfigDict(from_attributes=True)
   
class Role(MyBaseModel):
   id: Union[int, None] = None
   role: Union[str, None] = None
   role_description: Union[str, None] = None

class RolePost(MyBaseModel):
   role: str
   role_description: Union[str, None] = None

class IdType(MyBaseModel):
   id: Union[int, None] = None
   id_type: Union[str, None] = None
   id_description: Union[str, None] = None

class IdTypePost(MyBaseModel):
   id_type: str
   id_description: Union[str, None] = None

class User(MyBaseModel):
   id: Union[int, None] = None
   username: Union[str, None] = None
   password: Union[str, None] = None
   email: Union[EmailStr, None] = None
   name: Union[str, None] = None
   role_id: Union[int, None] = None
   role: Optional[Role]
   id_type_id: Union[int, None] = None
   id_type: Optional[IdType]
   id_number: Union[str, None] = None
   phone: Union[str, None] = None
   address: Union[str, None] = None

   status: Union[str, None] = None
   creator: Union[int, None] = None
   created_at: Union[datetime.datetime, None] = None
   editor: Union[int, None] = None
   updated_at: Union[datetime.datetime, None] = None

class UserPost(MyBaseModel):
   username: str
   password: str
   email: EmailStr
   name: str
   role_id: Union[int, None] = None
   id_type_id: Union[int, None] = None
   id_number: Union[str, None] = None
   phone: Union[str, None] = None
   address: Union[str, None] = None
