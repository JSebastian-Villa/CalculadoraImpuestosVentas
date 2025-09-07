# src/model/calculadora.py

"""
Módulo: calculadora
-------------------
Contiene la lógica de negocio para calcular el subtotal, el impuesto y el total de una compra.
Incluye validaciones de entrada y excepciones personalizadas para manejar errores comunes.

Excepciones definidas:
- ErrorPorcentajeImpuestoInvalido: cuando el impuesto no está en el rango [0, 1].
- ErrorPrecioNegativo: cuando el valor del producto es menor o igual a 0.
- ErrorCantidadNegativa: cuando la cantidad de productos es menor o igual a 0.

Funciones:
- validar_datos(valor_producto, cantidad, impuesto): valida que los parámetros sean correctos.
- calcular(valor_producto, cantidad, impuesto): calcula subtotal, impuesto y total.
"""


class ErrorPorcentajeImpuestoInvalido(Exception):
    def __init__(self, impuesto):
        super().__init__(
            f"Impuesto inválido. Debe estar entre 0% y 100%. "
            f"Actualmente, usted ingresó {impuesto * 100}%."
        )


class ErrorPrecioNegativo(Exception):
    def __init__(self, valor):
        super().__init__(
            f"Precio inválido. Debe ser mayor que 0. "
            f"Actualmente, usted ingresó {valor}."
        )


class ErrorCantidadNegativa(Exception):
    def __init__(self, cantidad):
        super().__init__(
            f"Cantidad inválida. Debe ser un número entero mayor que 0. "
            f"Actualmente, usted ingresó {cantidad}."
        )


def validar_datos(valor_producto, cantidad, impuesto):
    """
    Valida que los datos de entrada sean correctos.

    Parámetros:
        valor_producto (float): Precio unitario del producto. Debe ser mayor a 0.
        cantidad (int): Número de productos. Debe ser mayor a 0.
        impuesto (float): Impuesto en proporción, entre 0 y 1 (ejemplo: 0.19 para 19%).

    Excepciones:
        ErrorPrecioNegativo
        ErrorCantidadNegativa
        ErrorPorcentajeImpuestoInvalido
    """
    if valor_producto <= 0:
        raise ErrorPrecioNegativo(valor_producto)
    if cantidad <= 0:
        raise ErrorCantidadNegativa(cantidad)
    if impuesto < 0 or impuesto > 1:
        raise ErrorPorcentajeImpuestoInvalido(impuesto)


def calcular(valor_producto, cantidad, impuesto):
    """
    Calcula el subtotal, el valor del impuesto y el total de una compra.

    Parámetros:
        valor_producto (float): Valor unitario del producto (positivo).
        cantidad (int): Número de productos (entero positivo).
        impuesto (float): Impuesto en proporción (ejemplo: 0.19 para 19%).

    Retorna:
        tuple: (subtotal, valor_impuesto, total)
    """
    validar_datos(valor_producto, cantidad, impuesto)
    subtotal = valor_producto * cantidad
    iva = subtotal * impuesto
    total = subtotal + iva
    return subtotal, iva, total

