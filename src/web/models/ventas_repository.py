from __future__ import annotations

from dataclasses import dataclass, asdict
from decimal import Decimal, ROUND_HALF_UP
from typing import List, Optional, Dict, Any

from model.conexion_db import get_connection  # es un context manager


@dataclass
class Venta:
    venta_id: int
    valor_unitario: Decimal
    cantidad: int
    impuesto: Decimal  # porcentaje, por ejemplo 19 = 19%
    subtotal: Decimal
    iva: Decimal
    total: Decimal

    @classmethod
    def from_db_row(cls, row: tuple[Any, ...]) -> "Venta":
        return cls(
            venta_id=row[0],
            valor_unitario=Decimal(row[1]),
            cantidad=row[2],
            impuesto=Decimal(row[3]),
            subtotal=Decimal(row[4]),
            iva=Decimal(row[5]),
            total=Decimal(row[6]),
        )

    def to_dict(self) -> Dict[str, Any]:
        datos = asdict(self)
        for key in ("valor_unitario", "impuesto", "subtotal", "iva", "total"):
            datos[key] = f"{datos[key]:.2f}"
        return datos


def _redondear(valor: Decimal) -> Decimal:
    return valor.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def _calcular_totales(
    valor_unitario: Decimal, cantidad: int, impuesto: Decimal
) -> tuple[Decimal, Decimal, Decimal]:
    subtotal = _redondear(valor_unitario * cantidad)
    tasa = impuesto / Decimal("100")
    iva = _redondear(subtotal * tasa)
    total = _redondear(subtotal + iva)
    return subtotal, iva, total


def crear_tablas() -> None:
    sql = """
    CREATE TABLE IF NOT EXISTS ventas (
      venta_id SERIAL PRIMARY KEY,
      valor_unitario NUMERIC(12,2) NOT NULL,
      cantidad INT NOT NULL,
      impuesto NUMERIC(6,4) NOT NULL,
      subtotal NUMERIC(14,2) NOT NULL,
      iva NUMERIC(14,2) NOT NULL,
      total NUMERIC(14,2) NOT NULL,
      created_at TIMESTAMP DEFAULT NOW(),
      updated_at TIMESTAMP DEFAULT NOW()
    );
    """

    # AQUÍ usamos el context manager correctamente
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)


def crear_venta(
    valor_unitario: Decimal, cantidad: int, impuesto: Decimal
) -> int:
    subtotal, iva, total = _calcular_totales(valor_unitario, cantidad, impuesto)

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO ventas (
                    valor_unitario, cantidad, impuesto,
                    subtotal, iva, total
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING venta_id;
                """,
                (
                    float(valor_unitario),
                    cantidad,
                    float(impuesto),
                    float(subtotal),
                    float(iva),
                    float(total),
                ),
            )
            venta_id = cur.fetchone()[0]
    return venta_id


def listar_ventas(venta_id: Optional[str] = None) -> List[Dict[str, Any]]:
    with get_connection() as conn:
        with conn.cursor() as cur:
            if venta_id:
                cur.execute(
                    """
                    SELECT venta_id, valor_unitario, cantidad, impuesto,
                           subtotal, iva, total
                    FROM ventas
                    WHERE venta_id = %s
                    ORDER BY created_at DESC;
                    """,
                    (venta_id,),
                )
            else:
                cur.execute(
                    """
                    SELECT venta_id, valor_unitario, cantidad, impuesto,
                           subtotal, iva, total
                    FROM ventas
                    ORDER BY created_at DESC;
                    """
                )
            rows = cur.fetchall()

    return [Venta.from_db_row(row).to_dict() for row in rows]


def obtener_venta(venta_id: int) -> Optional[Dict[str, Any]]:
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT venta_id, valor_unitario, cantidad, impuesto,
                       subtotal, iva, total
                FROM ventas
                WHERE venta_id = %s;
                """,
                (venta_id,),
            )
            row = cur.fetchone()

    if row is None:
        return None
    return Venta.from_db_row(row).to_dict()


def actualizar_venta(
    venta_id: int,
    valor_unitario: Decimal,
    cantidad: int,
    impuesto: Decimal,
) -> None:
    subtotal, iva, total = _calcular_totales(valor_unitario, cantidad, impuesto)

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE ventas
                SET valor_unitario = %s,
                    cantidad = %s,
                    impuesto = %s,
                    subtotal = %s,
                    iva = %s,
                    total = %s,
                    updated_at = NOW()
                WHERE venta_id = %s;
                """,
                (
                    float(valor_unitario),
                    cantidad,
                    float(impuesto),
                    float(subtotal),
                    float(iva),
                    float(total),
                    venta_id,
                ),
            )
