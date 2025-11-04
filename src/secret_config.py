# src/secret_config.py
from __future__ import annotations

from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

if ENV_PATH.exists():
    load_dotenv(ENV_PATH)

def get_db_settings() -> dict[str, str]:
    return {
        "DB_NAME": os.getenv("DB_NAME", "calculadora_impuestos_ventas"),
        "DB_USER": os.getenv("DB_USER", "calculadora_impuestos_ventas_user"),
        "DB_PASSWORD": os.getenv("DB_PASSWORD", ""),
        "DB_HOST": os.getenv("DB_HOST", "dpg-d452ck2li9vc7387l9og-a.virginia-postgres.render.com"),
        "DB_PORT": os.getenv("DB_PORT", "5432"),
    }
