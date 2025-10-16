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

class TestSearchVentaController(unittest.TestCase):

    def setUp(self):
        """Limpia la tabla antes de cada caso."""
        clear_sql = (SQL_DIR / "00_clear.sql").read_text()
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute(clear_sql)

    # Helper para crear una venta base y devolver (id, venta_esperada)
    def _crear(self, vu, cant, imp):
        v = Venta.from_values(valor_unitario=vu, cantidad=cant, impuesto=imp)
        vid = VentaController.crear(v)
        return vid, v

    # 1) Buscar por ID luego de insertar una venta
    def test_buscar_por_id_ok(self):
        vid, esperado = self._crear(10000.0, 5, 0.19)
        obtenido = VentaController.buscar_por_id(vid)
        self.assertTrue(obtenido.is_equal(esperado))

    # 2) Listar varias ventas y validar cantidad + orden por ID
    def test_listar_varias_ok(self):
        ids = []
        for i in range(1, 4):
            vid, _ = self._crear(vu=1000.0 * i, cant=i, imp=0.19)
            ids.append(vid)

        lista = VentaController.listar()
        self.assertEqual(len(lista), 3)
        # Orden por venta_id creciente
        self.assertEqual([v.venta_id for v in lista], ids)

    # 3) Insertar 3 ventas y verificar que buscar_por_id trae la correcta (la del medio)
    def test_buscar_por_id_en_varias_ok(self):
        v1_id, v1 = self._crear(2500.0, 2, 0.19)
        v2_id, v2 = self._crear(3000.0, 3, 0.05)   # la que verificaremos
        v3_id, v3 = self._crear(1500.0, 1, 0.00)

        obtenido = VentaController.buscar_por_id(v2_id)
        self.assertTrue(obtenido.is_equal(v2))

if __name__ == "__main__":
    unittest.main(verbosity=2)
