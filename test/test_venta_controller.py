import unittest, pathlib, os, sys

# Asegura importar desde la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.model.conexion_db import get_conn
from src.controller.venta_controller import VentaController
from src.model.entities.venta import Venta

SQL_DIR = pathlib.Path("sql")

def setUpModule():
    """Crea las tablas una sola vez para todos los tests de este módulo."""
    create_sql = (SQL_DIR / "01_create_ventas.sql").read_text()
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(create_sql)

class TestInsertVentaController(unittest.TestCase):

    def setUp(self):
        """Limpia la tabla antes de cada caso."""
        clear_sql = (SQL_DIR / "00_clear.sql").read_text()
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute(clear_sql)

    # ---- Caso 1: inserción básica (19%) ----
    def test_insert_basico_ok(self):
        v = Venta.from_values(valor_unitario=10000.0, cantidad=5, impuesto=0.19)
        new_id = VentaController.crear(v)
        got = VentaController.buscar_por_id(new_id)
        self.assertTrue(got.is_equal(v))

    # ---- Caso 2: exento (0%) con cantidad 1 ----
    def test_insert_impuesto_cero_ok(self):
        v = Venta.from_values(valor_unitario=2500.0, cantidad=1, impuesto=0.0)
        vid = VentaController.crear(v)
        got = VentaController.buscar_por_id(vid)
        self.assertTrue(got.is_equal(v))
        self.assertEqual(got.subtotal, 2500.00)
        self.assertEqual(got.iva, 0.00)
        self.assertEqual(got.total, 2500.00)

    # ---- Caso 3: verifica redondeos a 2 decimales ----
    def test_insert_redondeo_ok(self):
        v = Venta.from_values(valor_unitario=3333.335, cantidad=3, impuesto=0.19)
        vid = VentaController.crear(v)
        got = VentaController.buscar_por_id(vid)
        self.assertTrue(got.is_equal(v))
        self.assertIsInstance(got.subtotal, float)
        self.assertIsInstance(got.iva, float)
        self.assertIsInstance(got.total, float)

if __name__ == "__main__":
    unittest.main(verbosity=2)
