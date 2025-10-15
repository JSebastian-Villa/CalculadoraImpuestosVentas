import sys
import os

# Agregar la raíz del proyecto al sys.path si no está
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from src.model import excepciones
except ModuleNotFoundError:
    import excepciones

def validar_datos(valor_producto, cantidad, impuesto):

    if valor_producto <= 0:
        raise excepciones.ErrorPrecioNegativo(valor_producto)
    if cantidad <= 0:
        raise excepciones.ErrorCantidadNegativa(cantidad)
    if impuesto < 0 or impuesto > 1:
        raise excepciones.ErrorPorcentajeImpuestoInvalido(impuesto)


def calcular(valor_producto, cantidad, impuesto):
    
    validar_datos(valor_producto, cantidad, impuesto)
    subtotal = valor_producto * cantidad
    iva = subtotal * impuesto
    total = subtotal + iva
    return subtotal, iva, total

class CalculadoraImpuestos:
    @staticmethod
    def calcular(valor_producto, cantidad, impuesto):
        return calcular(valor_producto, cantidad, impuesto)

