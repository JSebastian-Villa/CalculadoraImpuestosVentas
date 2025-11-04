# src/secret_config.py
from __future__ import annotations

from pathlib import Path
from typing import Dict
import os

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

# Si hay .env, lo cargamos (uso local)
if ENV_PATH.exists():
    load_dotenv(ENV_PATH)


# ⚠️ Datos de la BD en Render (fallback por defecto)
RENDER_DEFAULT_SETTINGS: Dict[str, str] = {
    "DB_NAME": "calculadora_impuestos_ventas",
    "DB_USER": "calculadora_impuestos_ventas_user",
    "DB_PASSWORD": "SzWp5I2J9lpwW7fxihQDmd9Xh3GUFFWI",
    "DB_HOST": "dpg-d452ck2li9vc7387l9og-a.virginia-postgres.render.com",
    "DB_PORT": "5432",
}


def get_db_settings() -> Dict[str, str]:
    """
    Prioridad:
    1. Si hay variables de entorno DB_* (o vienen de .env), se usan esas.
    2. Si no hay nada configurado, se usa por defecto la BD de Render
       (RENDER_DEFAULT_SETTINGS), para que el proyecto funcione
       directamente después de clonarlo.
    """
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")

    if all([db_name, db_user, db_password, db_host, db_port]):
        return {
            "DB_NAME": db_name,
            "DB_USER": db_user,
            "DB_PASSWORD": db_password,
            "DB_HOST": db_host,
            "DB_PORT": db_port,
        }

    # Sin configuración → usar Render por defecto
    return RENDER_DEFAULT_SETTINGS
