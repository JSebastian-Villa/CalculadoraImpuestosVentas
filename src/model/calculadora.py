class ErrorPorcentajeImpuestoInvalido(Exception):
    """Error cuando el impuesto es mayor a 100%"""


class ErrorPrecioNegativo(Exception):
    """Error cuando el valor del precio es negativo"""


class ErrorCantidadNegativa(Exception):
    """Error caundo la cantidad de productos es negativa"""


def validar_datos(valor_producto, cantidad, impuesto):
    if valor_producto <= 0:
        raise ErrorPrecioNegativo("Error: valor del producto inválido")
    if cantidad <= 0:
        raise ErrorCantidadNegativa("Error: cantidad inválida")
    if impuesto < 0 or impuesto > 1:
        raise ErrorPorcentajeImpuestoInvalido("Error: impuesto inválido")

# Función para realizar los cálculos
def calcular(valor_producto, cantidad, impuesto):
    validar_datos(valor_producto, cantidad, impuesto)
    subtotal = valor_producto * cantidad
    iva = subtotal * impuesto
    total = subtotal + iva
    return subtotal, iva, total


