# database.py
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Reemplaza 'username' con tu usuario de MySQL y 'mi_base_datos' con el nombre de tu base de datos
DATABASE_URL = "mysql+pymysql://root@127.0.0.1:3306/fastapidb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def test_conxion():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Conexion ok", result.scalar()==1)
    except Exception as e:
        print("error de conexion", e)


































    