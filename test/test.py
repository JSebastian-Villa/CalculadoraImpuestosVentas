
import unittest
from src.model.calculadora import (
    calcular,
    ErrorPrecioNegativo,
    ErrorCantidadNegativa,
    ErrorPorcentajeImpuestoInvalido,
)


class Pruebas(unittest.TestCase):

    def test_error_precio_negativo(self):
        # Entradas
        compra = -10_000
        cantidad = 3
        impuesto = 0.19

        # Proceso
        # Paso 1: Crear el bloque with, llamando a self.assertRaises
        with self.assertRaises(ErrorPrecioNegativo):
            # Paso 2: Llamar la función
            calcular(compra, cantidad, impuesto)

    def test_error_cantidad_negativo(self):
        # Entradas
        compra = 20_000
        cantidad = -5
        impuesto = 0.19

        # Proceso
        # Paso 1: Crear el bloque with, llamando a self.assertRaises
        with self.assertRaises(ErrorCantidadNegativa):
            # Paso 2: Llamar la función
            calcular(compra, cantidad, impuesto)

    def test_error_porcentaje_impuesto_invalido(self):
        # Entradas
        compra = 3_000
        cantidad = 3
        impuesto = 1.1  # 110%

        # Proceso
        # Paso 1: Crear el bloque with, llamando a self.assertRaises
        with self.assertRaises(ErrorPorcentajeImpuestoInvalido):
            # Paso 2: Llamar la función
            calcular(compra, cantidad, impuesto)

    def test_normal_1(self):
        # Entradas
        valor_producto = 10_000
        cantidad = 5
        impuesto = 0.19

        # Probar Proceso (usar el total devuelto por la función)
        _, _, cuota_calculada = calcular(valor_producto, cantidad, impuesto)

        # Verificar Salidas
        cuota_esperada = 59_500
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, places=0)

    def test_normal_2(self):
        # Entradas
        valor_producto = 5_000
        cantidad = 4
        impuesto = 0.19

        # Probar Proceso (usar el total devuelto por la función)
        _, _, cuota_calculada = calcular(valor_producto, cantidad, impuesto)

        # Verificar Salidas
        cuota_esperada = 23_800
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, places=0)

    def test_normal_3(self):
        # Entradas
        valor_producto = 6_000
        cantidad = 3
        impuesto = 0.05

        # Probar Proceso (usar el total devuelto por la función)
        _, _, cuota_calculada = calcular(valor_producto, cantidad, impuesto)

        # Verificar Salidas
        cuota_esperada = 18_900
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, places=0)

    # Casos extraordinarios
    def test_extraordinario_1_impuesto_excesivo(self):
        # Entradas
        valor_producto = 15_000
        cantidad = 2
        impuesto = 1.5  # 150%

        # Proceso + salida esperada
        with self.assertRaises(ErrorPorcentajeImpuestoInvalido):
            calcular(valor_producto, cantidad, impuesto)

    def test_extraordinario_2_cantidad_negativa(self):
        # Entradas
        valor_producto = 8_000
        cantidad = -3  # inválida
        impuesto = 0.19

        # Proceso + salida esperada
        with self.assertRaises(ErrorCantidadNegativa):
            calcular(valor_producto, cantidad, impuesto)

    def test_extraordinario_3_valor_producto_cero(self):
        # Entradas
        valor_producto = 0
        cantidad = 5
        impuesto = 0.05

        # Proceso + salida esperada
        with self.assertRaises(ErrorPrecioNegativo):
            calcular(valor_producto, cantidad, impuesto)


if __name__ == '__main__':
    unittest.main()
