# models.py
from sqlalchemy import Column, Integer, String
from database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), index=True)
    direccion = Column(String(100))
    telefono = Column(String(15))
    email = Column(String(50))
