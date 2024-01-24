from pydantic import BaseModel
from typing import Union


class Erro(BaseModel):
   detail: str