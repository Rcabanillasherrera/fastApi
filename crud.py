# crud.py
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Cliente
from schemas import ClienteCreate

#seleccionar cliente
def get_cliente(db: Session, cliente_id: int):
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()

#listar clientes
def get_clientes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Cliente).offset(skip).limit(limit).all()

#crear un cliente
def create_cliente(db: Session, cliente: ClienteCreate):
    db_cliente = Cliente(
        #manera antigua -> **cliente.dict()
        nombre = cliente.nombre,
        direccion = cliente.direccion,
        telefono = cliente.telefono,
        email = cliente.email   
        )
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

#actualizar cliente
def update_cliente(db: Session, cliente_id: int, cliente: ClienteCreate):
    db_cliente = get_cliente(db, cliente_id)
    if db_cliente:
        db_cliente.nombre = cliente.nombre
        db_cliente.direccion = cliente.direccion
        db_cliente.telefono = cliente.telefono
        db_cliente.email = cliente.email
        db.commit()
        db.refresh(db_cliente)
    return db_cliente

#eliminar un cliente
def delete_cliente(db: Session, cliente_id: int):
    db_cliente = get_cliente(db, cliente_id)
    if db_cliente:
        db.delete(db_cliente)
        db.commit()
    return db_cliente


#funciones PostgreSQL

async def get_cliente_postgresql(db: AsyncSession, cliente_id: int):

  result = await db.execute(select(Cliente).filter(Cliente.id == cliente_id))

  return result.scalar_one_or_none()



async def get_clientes_postgresql(db: AsyncSession, skip: int = 0, limit: int = 10):

  result = await db.execute(select(Cliente).offset(skip).limit(limit))

  return result.scalars().all()



async def create_cliente_postgresql(db: AsyncSession, cliente: ClienteCreate):

  db_cliente = Cliente(

    nombre=cliente.nombre,

    direccion=cliente.direccion,

    telefono=cliente.telefono,

    email=cliente.email

  )

  db.add(db_cliente)

  await db.commit()

  await db.refresh(db_cliente)

  return db_cliente



async def update_cliente_postgresql(db: AsyncSession, cliente_id: int, cliente: ClienteCreate):

  db_cliente = await get_cliente_postgresql(db, cliente_id)

  if db_cliente:

    db_cliente.nombre = cliente.nombre

    db_cliente.direccion = cliente.direccion

    db_cliente.telefono = cliente.telefono

    db_cliente.email = cliente.email

    await db.commit()

    await db.refresh(db_cliente)

  return db_cliente



async def delete_cliente_postgresql(db: AsyncSession, cliente_id: int):

  db_cliente = await get_cliente_postgresql(db, cliente_id)

  if db_cliente:

    await db.delete(db_cliente)

    await db.commit()

  return db_cliente



#end funciones PostgreSQL