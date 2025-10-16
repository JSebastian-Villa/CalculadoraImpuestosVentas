# src/model/conexion_db.py
import psycopg2
import os
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

def get_connection():
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("PG_DB"),
            user=os.getenv("PG_USER"),
            password=os.getenv("PG_PASSWORD"),
            host=os.getenv("PG_HOST"),
            port=os.getenv("PG_PORT")
        )
        print("Conexión exitosa a la base de datos")
        return connection
    except Exception as e:
        print(" Error al conectar con la base de datos:", e)
        return None
