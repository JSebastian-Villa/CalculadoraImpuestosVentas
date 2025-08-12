import unittest
import calculadora

class Pruebas(unittest.TestCase):

    def test_normal_1(self):
        #Entradas
        valor_producto = 10_000
        cantidad = 5
        impuesto = 0.19

        #Probar Proceso

        cuota_calculada = calculadora.calcular( valor_producto, cantidad , impuesto)

        #Verificar Salidas
        cuota_esperada = 59_500

        self.assertAlmostEqual( cuota_calculada, cuota_esperada, 0)
        
        
    def test_normal_2(self):
        
        # Entradas
        valor_producto = 5_000
        cantidad = 4
        impuesto = 0.19

        # Probar Proceso
        cuota_calculada = calculadora.calcular(valor_producto, cantidad, impuesto)

        # Verificar Salidas
        cuota_esperada = 23_800
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 0)
        
        
    def test_normal_3(self):
        # Entradas
        valor_producto = 6_000
        cantidad = 3
        impuesto = 0.05

        # Probar Proceso
        cuota_calculada = calculadora.calcular(valor_producto, cantidad, impuesto)

        # Verificar Salidas
        cuota_esperada = 18_900
        self.assertAlmostEqual(cuota_calculada, cuota_esperada, 0)
        
        
#testCasos extraordinarios
    
    def test_extraordinario_1_impuesto_excesivo(self):
        valor_producto = 15_000
        cantidad = 2
        impuesto = 1.5  # 150%
        salida_esperada = "Error: impuesto inválido"
        resultado = calculadora.calcular(valor_producto, cantidad, impuesto)
        self.assertEqual(resultado, salida_esperada)

    def test_extraordinario_2_cantidad_negativa(self):
        valor_producto = 8_000
        cantidad = -3  # inválida
        impuesto = 0.19
        salida_esperada = "Error: cantidad inválida"
        resultado = calculadora.calcular(valor_producto, cantidad, impuesto)
        self.assertEqual(resultado, salida_esperada)

    def test_extraordinario_3_valor_producto_cero(self):
        valor_producto = 0
        cantidad = 5
        impuesto = 0.05
        salida_esperada = "Error: valor del producto inválido"
        resultado = calculadora.calcular(valor_producto, cantidad, impuesto)
        self.assertEqual(resultado, salida_esperada)



if __name__ == '__main__':unittest.main()