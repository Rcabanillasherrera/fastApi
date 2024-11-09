# database.py
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base #MYSQL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine #POSTGRESQL
from sqlalchemy.orm import sessionmaker

# Reemplaza 'username' con tu usuario de MySQL y 'mi_base_datos' con el nombre de tu base de datos
MYSQL_DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost:5432/ahorroperu"
POSTGRESQL_DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost:5432/dbpy"

#MOTOR MYSQL
engine = create_engine(POSTGRESQL_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#MOTOR DE POSTGRESQL
postgresql_engine = create_async_engine(POSTGRESQL_DATABASE_URL, echo=True)
PostgreSQLSessionLocal = sessionmaker(autocommit=False, autoflush=False, bin=postgresql_engine, class_=AsyncSession)

#DECLARACION DE BASE DE DATOS
Base = declarative_base()


def test_conxion():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Conexion ok", result.scalar()==1)
    except Exception as e:
        print("error de conexion", e)


































    