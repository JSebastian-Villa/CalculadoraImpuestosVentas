# src/controller/venta_controller.py
from typing import List
from src.model.conexion_db import get_conn
from src.model.entities.venta import Venta
from src.model.excepciones import VentaNotFound

# Columnas proyectadas por todos los SELECT (respeta el orden esperado por Venta.from_db_row)
_FIELDS = """
venta_id, valor_unitario, cantidad, impuesto, subtotal, iva, total, created_at, updated_at
"""

class VentaController:
    """Casos de uso CRUD para la entidad Venta."""

    @staticmethod
    def crear(venta: Venta) -> int:
        """
        Inserta una venta y retorna el nuevo ID.
        Requiere que subtotal/iva/total vengan ya calculados en el modelo.
        """
        venta.validate()
        sql = """
            INSERT INTO ventas (valor_unitario, cantidad, impuesto, subtotal, iva, total)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING venta_id;
        """
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute(sql, venta.to_insert_tuple())
            new_id = cur.fetchone()[0]
            return new_id

    @staticmethod
    def actualizar(venta: Venta) -> None:
        """
        Actualiza una venta existente. Lanza VentaNotFound si no existe.
        """
        if venta.venta_id is None:
            raise ValueError("venta_id es requerido para actualizar")
        venta.validate()
        sql = """
            UPDATE ventas
               SET valor_unitario=%s,
                   cantidad=%s,
                   impuesto=%s,
                   subtotal=%s,
                   iva=%s,
                   total=%s,
                   updated_at=NOW()
             WHERE venta_id=%s;
        """
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute(sql, venta.to_update_tuple())
            if cur.rowcount == 0:
                raise VentaNotFound("Venta no encontrada para actualización")

    @staticmethod
    def borrar(venta_id: int) -> None:
        """
        Elimina una venta por ID. Lanza VentaNotFound si no existe.
        """
        sql = "DELETE FROM ventas WHERE venta_id=%s;"
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute(sql, (venta_id,))
            if cur.rowcount == 0:
                raise VentaNotFound("Venta no encontrada para borrado")

    @staticmethod
    def buscar_por_id(venta_id: int) -> Venta:
        """
        Retorna una Venta por ID o lanza VentaNotFound si no existe.
        """
        sql = f"SELECT {_FIELDS} FROM ventas WHERE venta_id=%s;"
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute(sql, (venta_id,))
            row = cur.fetchone()
            if not row:
                raise VentaNotFound("Venta no encontrada")
            return Venta.from_db_row(row)

    @staticmethod
    def listar() -> List[Venta]:
        """
        Retorna todas las ventas ordenadas por ID.
        """
        sql = f"SELECT {_FIELDS} FROM ventas ORDER BY venta_id;"
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
            return [Venta.from_db_row(r) for r in rows]
