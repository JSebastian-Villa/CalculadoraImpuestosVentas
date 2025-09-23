import sys 
sys.path.append("src")

from model import excepciones

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

