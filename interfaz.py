from calculadora import (
    calcular,
    ErrorPrecioNegativo,
    ErrorCantidadNegativa,
    ErrorPorcentajeImpuestoInvalido,
)


def interfaz_consola():
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