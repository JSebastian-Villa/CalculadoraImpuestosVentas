# ventas.py
from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from math import isclose


@dataclass(slots=True)
class Venta:
    """
    Entidad de dominio para una venta.
    Todos los montos se manejan como float con redondeo a 2 decimales.
    """
    venta_id: Optional[int]
    valor_unitario: float
    cantidad: int
    impuesto: float           # proporción 0..1
    subtotal: float
    iva: float
    total: float
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    # ---------- Utilidades de comparación ----------
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

    # ---------- Validación y redondeo ----------
    def validate(self) -> None:
        if self.valor_unitario < 0:
            raise ValueError("valor_unitario no puede ser negativo")
        if self.cantidad < 0:
            raise ValueError("cantidad no puede ser negativa")
        if not (0 <= self.impuesto <= 1):
            raise ValueError("impuesto debe estar entre 0 y 1")

    @staticmethod
    def _round2(x: float) -> float:
        # Evita errores binarios típicos del round directo en floats
        return float(f"{x:.2f}")

    # ---------- Fábricas y mapeos ----------
    @classmethod
    def from_values(cls, *, valor_unitario: float, cantidad: int, impuesto: float) -> "Venta":
        """
        Crea una Venta calculando subtotal, iva y total de forma consistente.
        """
        if cantidad < 0 or valor_unitario < 0:
            raise ValueError("valor_unitario y cantidad deben ser >= 0")
        if not (0 <= impuesto <= 1):
            raise ValueError("impuesto debe estar entre 0 y 1")

        subtotal = cls._round2(valor_unitario * cantidad)
        iva = cls._round2(subtotal * impuesto)
        total = cls._round2(subtotal + iva)

        v = cls(
            venta_id=None,
            valor_unitario=float(valor_unitario),
            cantidad=int(cantidad),
            impuesto=float(impuesto),
            subtotal=subtotal,
            iva=iva,
            total=total
        )
        v.validate()
        return v

    @classmethod
    def from_db_row(cls, row: tuple) -> "Venta":
        """
        Crea una Venta desde una fila devuelta por SELECT con columnas:
        (venta_id, valor_unitario, cantidad, impuesto, subtotal, iva, total, created_at, updated_at)
        """
        return cls(
            venta_id=row[0],
            valor_unitario=float(row[1]),
            cantidad=int(row[2]),
            impuesto=float(row[3]),
            subtotal=float(row[4]),
            iva=float(row[5]),
            total=float(row[6]),
            created_at=row[7],
            updated_at=row[8],
        )

    # ---------- Serialización para SQL ----------
    def to_insert_tuple(self) -> tuple:
        """Parámetros para INSERT (sin id)."""
        self.validate()
        return (
            self.valor_unitario, self.cantidad, self.impuesto,
            self.subtotal, self.iva, self.total
        )

    def to_update_tuple(self) -> tuple:
        """Parámetros para UPDATE (incluye id al final)."""
        if self.venta_id is None:
            raise ValueError("venta_id es requerido para actualizar")
        self.validate()
        return (
            self.valor_unitario, self.cantidad, self.impuesto,
            self.subtotal, self.iva, self.total, self.venta_id
        )
