# src/model/calculadora.py
"""
Módulo de cálculo de totales para ventas.

Contrato (según pruebas unitarias):
- validar_datos(valor, cantidad, impuesto) valida reglas de negocio.
- calcular(valor, cantidad, impuesto) -> (subtotal, iva, total) con redondeo a 2 decimales.
- Clase envoltorio CalculadoraImpuestos.calcular(...) que delega en calcular.

Reglas:
- valor_producto > 0           -> ErrorPrecioNegativo si no se cumple
- cantidad > 0                 -> ErrorCantidadNegativa si no se cumple
- 0 <= impuesto <= 1           -> ErrorPorcentajeImpuestoInvalido si no se cumple
"""

from typing import Tuple
from src.model.excepciones import (
    ErrorPrecioNegativo,
    ErrorCantidadNegativa,
    ErrorPorcentajeImpuestoInvalido,
)


def validar_datos(valor_producto: float, cantidad: int, impuesto: float) -> None:
    """Valida las reglas de negocio para el cálculo."""
    if valor_producto <= 0:
        raise ErrorPrecioNegativo(valor_producto)
    if cantidad <= 0:
        raise ErrorCantidadNegativa(cantidad)
    if not (0 <= impuesto <= 1):
        raise ErrorPorcentajeImpuestoInvalido(impuesto)


def calcular(valor_producto: float, cantidad: int, impuesto: float) -> Tuple[float, float, float]:
    """
    Calcula (subtotal, iva, total) con redondeo a 2 decimales.
    """
    validar_datos(valor_producto, cantidad, impuesto)

    subtotal = round(float(valor_producto) * int(cantidad), 2)
    iva = round(subtotal * float(impuesto), 2)
    total = round(subtotal + iva, 2)
    return subtotal, iva, total


class CalculadoraImpuestos:
    @staticmethod
    def calcular(valor_producto: float, cantidad: int, impuesto: float) -> Tuple[float, float, float]:
        """Wrapper estático para compatibilidad con la interfaz pedida."""
        return calcular(valor_producto, cantidad, impuesto)


__all__ = ["validar_datos", "calcular", "CalculadoraImpuestos"]
