import unittest, pathlib, os, sys

# Importar desde la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.model.conexion_db import get_conn
from src.controller.venta_controller import VentaController
from src.model.entities.venta import Venta

SQL_DIR = pathlib.Path("sql")

def setUpModule():
    """Deja el esquema correcto antes de todos los tests de este módulo."""
    ddl = (SQL_DIR / "00_drop_and_create_ventas.sql").read_text()
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(ddl)

class TestUpdateVentaController(unittest.TestCase):

    def setUp(self):
        """Limpia la tabla antes de cada caso."""
        clear_sql = (SQL_DIR / "00_clear.sql").read_text()
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute(clear_sql)

    # Helper para crear una venta base
    def _crear_base(self, vu=10000.0, cant=5, imp=0.19) -> int:
        v = Venta.from_values(valor_unitario=vu, cantidad=cant, impuesto=imp)
        return VentaController.crear(v)

    # 1) Cambiar cantidad, recalculando totales
    def test_update_cantidad_ok(self):
        vid = self._crear_base(vu=10000.0, cant=5, imp=0.19)

        v_mod = Venta.from_values(valor_unitario=10000.0, cantidad=6, impuesto=0.19)
        v_mod.venta_id = vid
        VentaController.actualizar(v_mod)

        got = VentaController.buscar_por_id(vid)
        self.assertTrue(got.is_equal(v_mod))

    # 2) Cambiar impuesto (19% -> 5%), recalculando totales
    def test_update_impuesto_ok(self):
        vid = self._crear_base(vu=6000.0, cant=3, imp=0.19)

        v_mod = Venta.from_values(valor_unitario=6000.0, cantidad=3, impuesto=0.05)
        v_mod.venta_id = vid
        VentaController.actualizar(v_mod)

        got = VentaController.buscar_por_id(vid)
        self.assertTrue(got.is_equal(v_mod))

    # 3) Cambiar valor unitario, recalculando totales
    def test_update_valor_unitario_ok(self):
        vid = self._crear_base(vu=2500.0, cant=2, imp=0.19)

        v_mod = Venta.from_values(valor_unitario=3000.0, cantidad=2, impuesto=0.19)
        v_mod.venta_id = vid
        VentaController.actualizar(v_mod)

        got = VentaController.buscar_por_id(vid)
        self.assertTrue(got.is_equal(v_mod))

if __name__ == "__main__":
    unittest.main(verbosity=2)
