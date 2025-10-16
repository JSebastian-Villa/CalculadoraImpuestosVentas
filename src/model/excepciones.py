# src/model/excepciones.py
"""
Excepciones de dominio y de infraestructura usadas en el proyecto.
Se proveen mensajes claros y parámetros opcionales para poder lanzar
las excepciones con o sin datos de contexto.
"""

from typing import Optional


class ErrorPorcentajeImpuestoInvalido(Exception):
    """El impuesto debe estar en el rango [0, 1]."""

    def __init__(self, impuesto: Optional[float] = None):
        if impuesto is None:
            msg = "Impuesto inválido. Debe estar entre 0% y 100%."
        else:
            msg = (
                "Impuesto inválido. Debe estar entre 0% y 100%. "
                f"Actualmente, usted ingresó {impuesto * 100}%."
            )
        super().__init__(msg)


class ErrorPrecioNegativo(Exception):
    """El precio/valor unitario debe ser > 0 (regla de negocio)."""

    def __init__(self, valor: Optional[float] = None):
        if valor is None:
            msg = "Precio inválido. Debe ser mayor que 0."
        else:
            msg = (
                "Precio inválido. Debe ser mayor que 0. "
                f"Actualmente, usted ingresó {valor}."
            )
        super().__init__(msg)


class ErrorCantidadNegativa(Exception):
    """La cantidad debe ser un entero > 0 (regla de negocio)."""

    def __init__(self, cantidad: Optional[int] = None):
        if cantidad is None:
            msg = "Cantidad inválida. Debe ser un número entero mayor que 0."
        else:
            msg = (
                "Cantidad inválida. Debe ser un número entero mayor que 0. "
                f"Actualmente, usted ingresó {cantidad}."
            )
        super().__init__(msg)


class VentaNotFound(Exception):
    """Se lanza cuando no se encuentra una venta en la base de datos."""
    pass


__all__ = [
    "ErrorPorcentajeImpuestoInvalido",
    "ErrorPrecioNegativo",
    "ErrorCantidadNegativa",
    "VentaNotFound",
]
