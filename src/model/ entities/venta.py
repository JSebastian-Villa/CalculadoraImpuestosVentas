# src/model/entities/venta.py
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass(slots=True)
class Venta:
    """Entidad de dominio que representa una fila de la tabla 'ventas'."""
    # Coinciden con columnas de la BD:
    venta_id: Optional[int]         # PK autoincremental (None mientras no se inserte)
    valor_unitario: float
    cantidad: int
    impuesto: float                 # proporción: 0.19 == 19%
    subtotal: float
    iva: float
    total: float
    created_at: Optional[datetime] = None   # Fecha y hora en que se creó el registro (se llena automáticamente al insertar en la BD)
    updated_at: Optional[datetime] = None   # Fecha y hora de la última actualización del registro (se actualiza cuando se modifica en la BD)
