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
