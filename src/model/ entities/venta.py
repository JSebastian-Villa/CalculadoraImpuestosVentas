from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from math import isclose

@dataclass(slots=True)
class Venta:
    venta_id: Optional[int]
    valor_unitario: float
    cantidad: int
    impuesto: float           # proporción 0..1
    subtotal: float
    iva: float
    total: float
    created_at: Optional[datetime] = None  # Fecha/hora de creación (la pone la BD)
    updated_at: Optional[datetime] = None  # Última modificación (la pone la BD)


    def is_equal(self, other: "Venta", *, tol: float = 1e-2) -> bool:
        """
        Compara dos ventas ignorando 'venta_id', 'created_at' y 'updated_at'.
        Para campos numéricos usa una tolerancia (por redondeos).
        """
        if not isinstance(other, Venta):
            return False

        return (
            self.cantidad == other.cantidad
            and isclose(self.valor_unitario, other.valor_unitario, rel_tol=0, abs_tol=tol)
            and isclose(self.impuesto, other.impuesto, rel_tol=0, abs_tol=1e-6)
            and isclose(self.subtotal, other.subtotal, rel_tol=0, abs_tol=tol)
            and isclose(self.iva, other.iva, rel_tol=0, abs_tol=tol)
            and isclose(self.total, other.total, rel_tol=0, abs_tol=tol)
        )
