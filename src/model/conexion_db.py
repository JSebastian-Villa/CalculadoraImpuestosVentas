# src/model/conexion_db.py
from contextlib import contextmanager
import psycopg2

# lee variables desde src/secret_config.py
try:
    # import absoluto (cuando se ejecuta el proyecto)
    from src.secret_config import get_db_settings
except ModuleNotFoundError:
    # fallback por si se ejecuta el módulo suelto
    from secret_config import get_db_settings


@contextmanager
def get_conn():
    """
    Entrega una conexión psycopg2 dentro de un context manager.
    - Hace commit si todo va bien.
    - Hace rollback y relanza la excepción si algo falla.
    - Cierra la conexión siempre al final.
    """
    cfg = get_db_settings()
    conn = psycopg2.connect(
        dbname=cfg["DB_NAME"],
        user=cfg["DB_USER"],
        password=cfg["DB_PASSWORD"],
        host=cfg["DB_HOST"],
        port=cfg["DB_PORT"],
    )
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


# Alias opcional por si en algún lugar lo importaste con otro nombre
get_connection = get_conn

__all__ = ["get_conn", "get_connection"]
