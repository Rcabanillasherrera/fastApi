#main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine
from models import Cliente
from schemas import Cliente, ClienteCreate
import crud

#Inicializar la aplicación
app = FastAPI()

#Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#Crear un cliente
@app.post("/clientes/", response_model=Cliente)
def create_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return crud.create_cliente(db=db, cliente=cliente)

#Obtener todos los clientes
@app.get("/clientes/", response_model=List[Cliente])
def read_clientes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_clientes(db, skip=skip, limit=limit)

#Obtener un cliente por ID
@app.get("/clientes/{cliente_id}", response_model=Cliente)
def read_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = crud.get_cliente(db, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente
#Actualizar un cliente
@app.put("/clientes/{cliente_id}", response_model=Cliente)
def update_cliente(cliente_id: int, cliente: ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = crud.update_cliente(db, cliente_id=cliente_id, cliente=cliente)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente

#Eliminar un cliente
@app.delete("/clientes/{cliente_id}", response_model=dict)
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = crud.delete_cliente(db, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return {"message": "Cliente eliminado"}

