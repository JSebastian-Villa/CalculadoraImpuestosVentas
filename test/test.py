"""
Módulo de pruebas unitarias para `src.model.calculadora`.

Este archivo valida:
- Manejo de errores con excepciones personalizadas:
  * ErrorPrecioNegativo
  * ErrorCantidadNegativa
  * ErrorPorcentajeImpuestoInvalido
- Cálculos correctos de subtotal, IVA y total en casos normales.

Convenciones:
- `impuesto` se pasa como proporción (0.19 = 19%).
- La función `calcular` retorna (subtotal, iva, total).
"""

import unittest
from src.model.calculadora import (
    calcular,
    ErrorPrecioNegativo,
    ErrorCantidadNegativa,
    ErrorPorcentajeImpuestoInvalido,
)


class Pruebas(unittest.TestCase):
    """Suite de pruebas para la función `calcular` del módulo `calculadora`."""

    def test_error_precio_negativo(self):
        """Debe lanzar ErrorPrecioNegativo cuando el precio es <= 0."""
        # Entradas
        valor_compra = -10_000
        cantidad = 3
        impuesto = 0.19

        # Proceso
        # Paso 1: Crear el bloque with, llamando a self.assertRaises
        with self.assertRaises(ErrorPrecioNegativo):
            # Paso 2: Llamar la función
            calcular(valor_compra, cantidad, impuesto)

    def test_error_cantidad_negativo(self):
        """Debe lanzar ErrorCantidadNegativa cuando la cantidad es <= 0."""
        # Entradas
        valor_compra = 20_000
        cantidad = -5
        impuesto = 0.19

        # Proceso
        # Paso 1: Crear el bloque with, llamando a self.assertRaises
        with self.assertRaises(ErrorCantidadNegativa):
            # Paso 2: Llamar la función
            calcular(valor_compra, cantidad, impuesto)

    def test_error_porcentaje_impuesto_invalido(self):
        """Debe lanzar ErrorPorcentajeImpuestoInvalido cuando impuesto no está en [0, 1]."""
        # Entradas
        valor_compra = 3_000
        cantidad = 3
        impuesto = 1.1  # 110%

        # Proceso
        # Paso 1: Crear el bloque with, llamando a self.assertRaises
        with self.assertRaises(ErrorPorcentajeImpuestoInvalido):
            # Paso 2: Llamar la función
            calcular(valor_compra, cantidad, impuesto)

    def test_normal_1(self):
        """Caso normal: 10_000 x 5 con 19% → total 59_500."""
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
        """Caso normal: 5_000 x 4 con 19% → total 23_800."""
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
        """Caso normal: 6_000 x 3 con 5% → total 18_900."""
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
        """Debe lanzar ErrorPorcentajeImpuestoInvalido con impuesto > 1 (150%)."""
        # Entradas
        valor_producto = 15_000
        cantidad = 2
        impuesto = 1.5  # 150%

        # Proceso + salida esperada
        with self.assertRaises(ErrorPorcentajeImpuestoInvalido):
            calcular(valor_producto, cantidad, impuesto)

    def test_extraordinario_2_cantidad_negativa(self):
        """Debe lanzar ErrorCantidadNegativa con cantidad negativa."""
        # Entradas
        valor_producto = 8_000
        cantidad = -3  # inválida
        impuesto = 0.19

        # Proceso + salida esperada
        with self.assertRaises(ErrorCantidadNegativa):
            calcular(valor_producto, cantidad, impuesto)

    def test_extraordinario_3_valor_producto_cero(self):
        """Debe lanzar ErrorPrecioNegativo si valor del producto es 0 (según regla de negocio)."""
        # Entradas
        valor_producto = 0
        cantidad = 5
        impuesto = 0.05

        # Proceso + salida esperada
        with self.assertRaises(ErrorPrecioNegativo):
            calcular(valor_producto, cantidad, impuesto)


if __name__ == '__main__':
    unittest.main()
