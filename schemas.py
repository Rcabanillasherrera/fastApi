# schemas.py
from pydantic import BaseModel

class ClienteBase(BaseModel):
    nombre: str
    direccion: str
    telefono: str
    email: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int

class Config:
    orm_mode = True

