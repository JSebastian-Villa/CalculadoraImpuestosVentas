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
    impuesto: Decimal  # porcentaje para la capa web (ej. 19 = 19 %)
    subtotal: Decimal
    iva: Decimal
    total: Decimal

    @classmethod
    def from_db_row(cls, row: tuple[Any, ...]) -> "Venta":
        """
        row[3] en BD es la TASA (ej. 0.19).
        Para la capa web lo convertimos a PORCENTAJE (19.00).
        """
        tasa = Decimal(row[3])           # 0.19 en BD
        impuesto_pct = tasa * Decimal("100")  # 19.00 para la web

        return cls(
            venta_id=row[0],
            valor_unitario=Decimal(row[1]),
            cantidad=row[2],
            impuesto=impuesto_pct,
            subtotal=Decimal(row[4]),
            iva=Decimal(row[5]),
            total=Decimal(row[6]),
        )

    def to_dict(self) -> Dict[str, Any]:
        datos = asdict(self)
        # formateamos decimales como string con 2 decimales
        for key in ("valor_unitario", "impuesto", "subtotal", "iva", "total"):
            datos[key] = f"{datos[key]:.2f}"
        return datos


def _redondear(valor: Decimal) -> Decimal:
    return valor.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def _calcular_totales(
    valor_unitario: Decimal, cantidad: int, impuesto_pct: Decimal
) -> tuple[Decimal, Decimal, Decimal, Decimal]:
    """
    impuesto_pct llega en PORCENTAJE (ej. 19).
    Convertimos a tasa fraccionaria para los cálculos y para guardar en BD.
    """
    tasa = impuesto_pct / Decimal("100")  # 19 -> 0.19
    subtotal = _redondear(valor_unitario * cantidad)
    iva = _redondear(subtotal * tasa)
    total = _redondear(subtotal + iva)
    return subtotal, iva, total, tasa


def crear_tablas() -> None:
    sql = """
    CREATE TABLE IF NOT EXISTS ventas (
      venta_id SERIAL PRIMARY KEY,
      valor_unitario NUMERIC(12,2) NOT NULL,
      cantidad INT NOT NULL,
      impuesto NUMERIC(6,4) NOT NULL,  -- tasa fraccionaria, ej. 0.19
      subtotal NUMERIC(14,2) NOT NULL,
      iva NUMERIC(14,2) NOT NULL,
      total NUMERIC(14,2) NOT NULL,
      created_at TIMESTAMP DEFAULT NOW(),
      updated_at TIMESTAMP DEFAULT NOW()
    );
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)


def crear_venta(
    valor_unitario: Decimal, cantidad: int, impuesto: Decimal
) -> int:
    """
    impuesto llega como PORCENTAJE desde el formulario (ej. 19).
    En BD se guarda como tasa (0.19) por la restricción CHECK.
    """
    subtotal, iva, total, tasa = _calcular_totales(valor_unitario, cantidad, impuesto)

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
                    float(tasa),       # <-- GUARDAMOS LA TASA (0.19), NO 19
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
    """
    impuesto llega como PORCENTAJE (ej. 19) desde el formulario.
    En BD se guarda como tasa (0.19).
    """
    subtotal, iva, total, tasa = _calcular_totales(valor_unitario, cantidad, impuesto)

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
                    float(tasa),       # <-- también aquí guardamos la TASA
                    float(subtotal),
                    float(iva),
                    float(total),
                    venta_id,
                ),
            )
