class ErrorPorcentajeImpuestoInvalido(Exception):
    def __init__(self, impuesto):
        super().__init__(f"Impuesto inválido. Debe estar entre 0% y 100%. Actualmente, usted ingresó {impuesto*100}%.")


class ErrorPrecioNegativo(Exception):
    def __init__(self, valor):
        super().__init__(f"Precio inválido. Debe ser mayor que 0. Actualmente, usted ingresó {valor}.")


class ErrorCantidadNegativa(Exception):
    def __init__(self, cantidad):
        super().__init__(f"Cantidad inválida. Debe ser un número entero mayor que 0. Actualmente, usted ingresó {cantidad}.")


def validar_datos(valor_producto, cantidad, impuesto):
    if valor_producto <= 0:
        raise ErrorPrecioNegativo(valor_producto)
    if cantidad <= 0:
        raise ErrorCantidadNegativa(cantidad)
    if impuesto < 0 or impuesto > 1:
        raise ErrorPorcentajeImpuestoInvalido(impuesto)


def calcular(valor_producto, cantidad, impuesto):
    validar_datos(valor_producto, cantidad, impuesto)
    subtotal = valor_producto * cantidad
    iva = subtotal * impuesto
    total = subtotal + iva
    return subtotal, iva, total
