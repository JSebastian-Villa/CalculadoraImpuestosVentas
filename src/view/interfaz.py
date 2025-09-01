"""
Módulo: interfaz_consola
------------------------
Vista de consola para la calculadora de IVA.
Este módulo permite al usuario ingresar datos desde la terminal y muestra los resultados
del cálculo de subtotal, IVA y total, manejando las posibles excepciones de entrada.
"""

import sys
sys.path.append("src")

from model.calculadora import (
    calcular,
    ErrorPrecioNegativo,
    ErrorCantidadNegativa,
    ErrorPorcentajeImpuestoInvalido,
)


def interfaz_consola():
    """
    Interfaz de usuario por consola para calcular el total de una compra con IVA.

    Flujo:
    - Solicita al usuario el valor del producto, la cantidad y el impuesto (%).
    - Convierte el impuesto a proporción (dividiendo entre 100).
    - Llama a la función `calcular` del modelo para obtener subtotal, IVA y total.
    - Muestra los resultados en pantalla con formato numérico.

    Manejo de errores:
    - ValueError: cuando el usuario ingresa datos no numéricos.
    - ErrorPrecioNegativo: si el precio ingresado es <= 0.
    - ErrorCantidadNegativa: si la cantidad ingresada es <= 0.
    - ErrorPorcentajeImpuestoInvalido: si el impuesto no está en [0, 100].
    """
    print("=== Calculadora de Total con IVA ===\n")
    try:
        valor = float(input("Ingresa el valor del producto: "))
        cantidad = int(input("Ingresa la cantidad: "))
        impuesto = float(input("Ingresa el impuesto (%): "))

        subtotal, iva, total = calcular(valor, cantidad, impuesto / 100)

        print(f"\nEl subtotal es: {subtotal:,.2f}")
        print(f"El IVA es: {iva:,.2f}")
        print(f"Total a pagar: {total:,.2f}")

    except ValueError:
        print("Error: debes ingresar números válidos.")
    except ErrorPrecioNegativo as e:
        print(f"{e}")
    except ErrorCantidadNegativa as e:
        print(f"{e}")
    except ErrorPorcentajeImpuestoInvalido as e:
        print(f"{e}")


if __name__ == "__main__":
    interfaz_consola()
