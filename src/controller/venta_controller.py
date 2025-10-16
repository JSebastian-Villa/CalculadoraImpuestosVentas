# src/controller/venta_controller.py
from psycopg2.extras import RealDictCursor
from src.model.entities.venta import Venta
from src.model.conexion_db import get_connection

def insertar_venta(v: Venta) -> int:
    sql = """
    INSERT INTO ventas (valor_unitario, cantidad, impuesto, subtotal, iva, total)
    VALUES (%s, %s, %s, %s, %s, %s)
    RETURNING venta_id;
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (v.valor_unitario, v.cantidad, v.impuesto,
                              v.subtotal, v.iva, v.total))
            new_id = cur.fetchone()[0]
    return new_id

def buscar_venta(venta_id: int) -> Venta | None:
    sql = "SELECT * FROM ventas WHERE venta_id = %s;"
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql, (venta_id,))
            row = cur.fetchone()
            return Venta(**row) if row else None

def modificar_venta(venta_id: int, v: Venta) -> bool:
    sql = """
    UPDATE ventas
       SET valor_unitario=%s, cantidad=%s, impuesto=%s,
           subtotal=%s, iva=%s, total=%s
     WHERE venta_id=%s;
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (v.valor_unitario, v.cantidad, v.impuesto,
                              v.subtotal, v.iva, v.total, venta_id))
            return cur.rowcount == 1

def borrar_venta(venta_id: int) -> bool:
    sql = "DELETE FROM ventas WHERE venta_id = %s;"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (venta_id,))
            return cur.rowcount == 1
