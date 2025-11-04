# src/secret_config.py
from __future__ import annotations

from pathlib import Path
from typing import Dict
from urllib.parse import urlparse
import os

from dotenv import load_dotenv


# Carga el .env de la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"
if env_path.exists():
    load_dotenv(env_path)


def _from_database_url(url: str) -> Dict[str, str]:
    """
    Parsea un DATABASE_URL tipo:
    postgres://user:pass@host:5432/dbname
    y lo convierte en las claves que usa conexion_db.
    """
    parsed = urlparse(url)

    return {
        "DB_NAME": parsed.path.lstrip("/") or "postgres",
        "DB_USER": parsed.username or "",
        "DB_PASSWORD": parsed.password or "",
        "DB_HOST": parsed.hostname or "localhost",
        "DB_PORT": str(parsed.port or 5432),
    }


def get_db_settings() -> Dict[str, str]:
    """
    Prioridad:
    1. Si existe DATABASE_URL -> la usa (ideal en Render).
    2. Si no, usa las variables DB_NAME, DB_USER, etc. del entorno/.env
       (ideal para local).
    """
    db_url = os.getenv("DATABASE_URL")
    if db_url:
        return _from_database_url(db_url)

    return {
        "DB_NAME": os.getenv("DB_NAME", "calculadora_impuestos"),
        "DB_USER": os.getenv("DB_USER", "postgres"),
        "DB_PASSWORD": os.getenv("DB_PASSWORD", ""),
        "DB_HOST": os.getenv("DB_HOST", "localhost"),
        "DB_PORT": os.getenv("DB_PORT", "5432"),
    }
