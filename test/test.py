import unittest
from src.model.calculadora import (
    calcular,
    ErrorPrecioNegativo,
    ErrorCantidadNegativa,
    ErrorPorcentajeImpuestoInvalido,
)

IMPUESTO_19 = 0.19
IMPUESTO_5 = 0.05
IMPUESTO_INVALIDO = 1.1  # 110%

VALOR_NEGATIVO = -10_000
VALOR_PRODUCTO_1 = 10_000
VALOR_PRODUCTO_2 = 5_000
VALOR_PRODUCTO_3 = 6_000
VALOR_PRODUCTO_EXTRA = 15_000
VALOR_PRODUCTO_CERO = 0
VALOR_PRODUCTO_8K = 8_000

CANTIDAD_1 = 5
CANTIDAD_2 = 4
CANTIDAD_3 = 3
CANTIDAD_EXTRA = 2
CANTIDAD_NEGATIVA = -5
CANTIDAD_NEGATIVA_2 = -3
CANTIDAD_5 = 5

TOTAL_ESPERADO_1 = 59_500
TOTAL_ESPERADO_2 = 23_800
TOTAL_ESPERADO_3 = 18_900


class Pruebas(unittest.TestCase):

    def test_error_precio_negativo(self):
        with self.assertRaises(ErrorPrecioNegativo):
            calcular(VALOR_NEGATIVO, CANTIDAD_3, IMPUESTO_19)

    def test_error_cantidad_negativo(self):
        with self.assertRaises(ErrorCantidadNegativa):
            calcular(VALOR_PRODUCTO_1 * 2, CANTIDAD_NEGATIVA, IMPUESTO_19)

    def test_error_porcentaje_impuesto_invalido(self):
        with self.assertRaises(ErrorPorcentajeImpuestoInvalido):
            calcular(VALOR_PRODUCTO_3, CANTIDAD_3, IMPUESTO_INVALIDO)

    def test_normal_1(self):
        _, _, cuota_calculada = calcular(VALOR_PRODUCTO_1, CANTIDAD_1, IMPUESTO_19)
        self.assertAlmostEqual(cuota_calculada, TOTAL_ESPERADO_1, places=0)

    def test_normal_2(self):
        _, _, cuota_calculada = calcular(VALOR_PRODUCTO_2, CANTIDAD_2, IMPUESTO_19)
        self.assertAlmostEqual(cuota_calculada, TOTAL_ESPERADO_2, places=0)

    def test_normal_3(self):
        _, _, cuota_calculada = calcular(VALOR_PRODUCTO_3, CANTIDAD_3, IMPUESTO_5)
        self.assertAlmostEqual(cuota_calculada, TOTAL_ESPERADO_3, places=0)

    def test_extraordinario_1_impuesto_excesivo(self):
        with self.assertRaises(ErrorPorcentajeImpuestoInvalido):
            calcular(VALOR_PRODUCTO_EXTRA, CANTIDAD_EXTRA, IMPUESTO_INVALIDO)

    def test_extraordinario_2_cantidad_negativa(self):
        with self.assertRaises(ErrorCantidadNegativa):
            calcular(VALOR_PRODUCTO_8K, CANTIDAD_NEGATIVA_2, IMPUESTO_19)

    def test_extraordinario_3_valor_producto_cero(self):
        with self.assertRaises(ErrorPrecioNegativo):
            calcular(VALOR_PRODUCTO_CERO, CANTIDAD_5, IMPUESTO_5)


if __name__ == '__main__':
    unittest.main()
