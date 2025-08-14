
import unittest
import calculadora


class Pruebas(unittest.TestCase):

    def test_error_precio_negativo(self):
        #entradas
        compra = -10_000
        cantidad = 3
        impuesto = 0.19

        #preceso
        #paso 1: Crear el bloque with, llamadi a self.assertRaises
        with self.assertRaises(calculadora.ErrorPrecioNegativo):
            #pase 2: LLamar la función
            calculadora.calcular(compra, cantidad, impuesto)

    def test_error_cantidad_negativo(self):
        #entradas
        compra = 20_000
        cantidad = -5
        impuesto = 0.19

        #preceso
        #paso 1: Crear el bloque with, llamadi a self.assertRaises
        with self.assertRaises(calculadora.ErrorCantidadNegativa):
            #pase 2: LLamar la función
            calculadora.calcular(compra, cantidad, impuesto)

    def test_error_porcentaje_impuesto_invalido(self):
        #entradas
        compra = 3_000
        cantidad = 3
        impuesto = 1.1

        #preceso
        #paso 1: Crear el bloque with, llamadi a self.assertRaises
        with self.assertRaises(calculadora.ErrorPorcentajeImpuestoInvalido):
            #pase 2: LLamar la función
            calculadora.calcular(compra, cantidad, impuesto)

    def test_normal_1(self):
        #Entradas
        valor_producto = 10_000
        cantidad = 5
        impuesto = 0.19

        #Probar Proceso (usar el total devuelto por la función)
        _, _, cuota_calculada = calculadora.calcular(valor_producto, cantidad, impuesto)

        #Verificar Salidas
        cuota_esperada = 59_500
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 0)

    def test_normal_2(self):
        # Entradas
        valor_producto = 5_000
        cantidad = 4
        impuesto = 0.19

        # Probar Proceso (usar el total devuelto por la función)
        _, _, cuota_calculada = calculadora.calcular(valor_producto, cantidad, impuesto)

        # Verificar Salidas
        cuota_esperada = 23_800
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 0)

    def test_normal_3(self):
        # Entradas
        valor_producto = 6_000
        cantidad = 3
        impuesto = 0.05

        # Probar Proceso (usar el total devuelto por la función)
        _, _, cuota_calculada = calculadora.calcular(valor_producto, cantidad, impuesto)

        # Verificar Salidas
        cuota_esperada = 18_900
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 0)

    #testCasos extraordinarios
    def test_extraordinario_1_impuesto_excesivo(self):
        valor_producto = 15_000
        cantidad = 2
        impuesto = 1.5  # 150%
        with self.assertRaises(calculadora.ErrorPorcentajeImpuestoInvalido):
            calculadora.calcular(valor_producto, cantidad, impuesto)

    def test_extraordinario_2_cantidad_negativa(self):
        valor_producto = 8_000
        cantidad = -3  # inválida
        impuesto = 0.19
        with self.assertRaises(calculadora.ErrorCantidadNegativa):
            calculadora.calcular(valor_producto, cantidad, impuesto)

    def test_extraordinario_3_valor_producto_cero(self):
        valor_producto = 0
        cantidad = 5
        impuesto = 0.05
        with self.assertRaises(calculadora.ErrorPrecioNegativo):
            calculadora.calcular(valor_producto, cantidad, impuesto)

if __name__ == '__main__':
    unittest.main()