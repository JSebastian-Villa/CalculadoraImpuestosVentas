# src/secret_config.py
import os
from typing import Dict
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

def _load_env() -> None:
    """
    Carga el archivo .env de forma robusta:
    - Primero intenta autodetectar con find_dotenv() (recorre hacia arriba).
    - Si no lo encuentra, intenta rutas conocidas (raíz del proyecto).
    """
    # 1) Autodetección 
    env_path = find_dotenv(usecwd=True)

    if not env_path:
        # 2) Intentos manuales (por si find_dotenv falla)
        candidates = [
            Path.cwd() / ".env",
            Path(__file__).resolve().parents[1] / ".env",
            Path(__file__).resolve().parents[2] / ".env",
        ]
        for c in candidates:
            if c.exists():
                env_path = str(c)
                break

    # Si aún no lo encontró, load_dotenv() aún puede cargar variables del entorno actual.
    load_dotenv(env_path if env_path else None)

def get_db_settings() -> Dict[str, str]:
    """
    Retorna las credenciales de BD desde variables de entorno.
    Acepta claves con prefijo DB_* y, en fallback, PG_* (por si tu .env usa ese prefijo).
    Lanza un error si falta alguna.
    """
    _load_env()

    def getenv_any(*keys):
        for k in keys:
            v = os.getenv(k)
            if v:
                return v
        return None

    cfg = {
        "DB_NAME": getenv_any("DB_NAME", "PG_DB"),
        "DB_USER": getenv_any("DB_USER", "PG_USER"),
        "DB_PASSWORD": getenv_any("DB_PASSWORD", "PG_PASSWORD"),
        "DB_HOST": getenv_any("DB_HOST", "PG_HOST"),
        "DB_PORT": getenv_any("DB_PORT", "PG_PORT"),
    }

    faltantes = [k for k, v in cfg.items() if not v]
    if faltantes:
        raise RuntimeError(f"Variables faltantes en .env: {faltantes}")

    return cfg
