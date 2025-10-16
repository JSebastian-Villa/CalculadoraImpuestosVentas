import unittest
from datetime import datetime, timedelta
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.model.entities.venta import Venta



class TestVentaEntity(unittest.TestCase):

    def test_is_equal_true_con_tolerancia(self):
        """Dos ventas equivalentes deben ser iguales aunque difieran en centavos."""
        a = Venta(
            venta_id=1,
            valor_unitario=10000.00,
            cantidad=5,
            impuesto=0.19,
            subtotal=50000.00,
            iva=9500.00,
            total=59500.00,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        # Variaciones mínimas dentro de la tolerancia (1e-2 por defecto)
        b = Venta(
            venta_id=99,  # id distinto no debe afectar
            valor_unitario=10000.001,
            cantidad=5,
            impuesto=0.19,
            subtotal=50000.004,
            iva=9499.999,
            total=59499.999,
            created_at=datetime.now() - timedelta(days=1),
            updated_at=datetime.now() - timedelta(minutes=5),
        )
        self.assertTrue(a.is_equal(b))

    def test_is_equal_false_por_cantidad(self):
        """Si cambia un campo de negocio (p. ej. cantidad), no son iguales."""
        a = Venta(None, 10000, 5, 0.19, 50000, 9500, 59500)
        c = Venta(None, 10000, 6, 0.19, 60000, 11400, 71400)
        self.assertFalse(a.is_equal(c))

    def test_is_equal_false_por_impuesto(self):
        """Cambio en el impuesto (0.19 vs 0.05) los hace distintos."""
        a = Venta(None, 6000, 3, 0.19, 18000, 3420, 21420)
        d = Venta(None, 6000, 3, 0.05, 18000, 900, 18900)
        self.assertFalse(a.is_equal(d))


if __name__ == "__main__":
    unittest.main()
