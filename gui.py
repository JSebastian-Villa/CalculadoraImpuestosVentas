# gui.py
"""
Interfaz de Usuario (CLI) – Insertar una Venta
- Pide valor_unitario, cantidad e impuesto (acepta 19, 19% o 0.19)
- Calcula subtotal, IVA y total
- Inserta en la BD y muestra el ID creado y el resumen
"""

from src.model.entities.venta import Venta
from src.controller.venta_controller import VentaController
from src.model.excepciones import (
    ErrorPrecioNegativo,
    ErrorCantidadNegativa,
    ErrorPorcentajeImpuestoInvalido,
)
import psycopg2


def _parse_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            return float(raw)
        except ValueError:
            print("Ingresa un número válido (usa punto o coma para decimales).")


def _parse_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            return val
        except ValueError:
            print("Ingresa un entero válido.")


def _parse_impuesto(prompt: str) -> float:
    """
    Acepta:
      - '19%'  -> 0.19
      - '19'   -> 0.19
      - '0.19' -> 0.19
    """
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            if raw.endswith("%"):
                num = float(raw[:-1])
                return round(num / 100.0, 4)
            num = float(raw)
            if num > 1:  # asumimos que tecleó porcentaje (ej: 19)
                return round(num / 100.0, 4)
            return num
        except ValueError:
            print("Ingresa un número válido (ej: 19, 19% o 0.19).")


def insertar_venta():
    print("\n=== Insertar venta ===")
    vu = _parse_float("Valor unitario: ")
    cant = _parse_int("Cantidad: ")
    imp = _parse_impuesto("Impuesto (19, 19% o 0.19): ")

    try:
        # Calcula subtotal/iva/total y valida reglas de negocio
        v = Venta.from_values(valor_unitario=vu, cantidad=cant, impuesto=imp)

        # Inserta en BD y devuelve el ID
        new_id = VentaController.crear(v)
        creada = VentaController.buscar_por_id(new_id)

        print("\nVenta creada correctamente.")
        print(f"ID: {creada.venta_id}")
        print(f"Valor unitario: {creada.valor_unitario:.2f}")
        print(f"Cantidad: {creada.cantidad}")
        print(f"Impuesto: {creada.impuesto * 100:.2f}%")
        print(f"Subtotal: {creada.subtotal:.2f}")
        print(f"IVA: {creada.iva:.2f}")
        print(f"Total: {creada.total:.2f}\n")

    except (ErrorPrecioNegativo, ErrorCantidadNegativa, ErrorPorcentajeImpuestoInvalido) as e:
        print(f"Error de validación: {e}")
    except psycopg2.Error as e:
        print("Error de base de datos:")
        print(f"    {e.__class__.__name__}: {e}")
    except Exception as e:
        print("Error inesperado:", e)


if __name__ == "__main__":
    # Ejecuta directamente la acción de insertar (foco en tu checklist)
    insertar_venta()
