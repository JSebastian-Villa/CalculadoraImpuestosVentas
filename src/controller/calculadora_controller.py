import sys
import os

# Asegurar que se pueda importar el modelo sin errores
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.model.calculadora import CalculadoraImpuestos
from src.model import excepciones


class CalculadoraController:
    """
    Controlador de la calculadora de impuestos.
    Se encarga de recibir los datos del usuario (desde la vista),
    validarlos y delegar el cálculo al modelo.
    """

    @staticmethod
    def calcular_impuesto(valor_producto: float, cantidad: int, impuesto: float):
        """
        Realiza el cálculo del subtotal, IVA y total de la venta.
        Maneja los errores definidos en excepciones.py
        """

        try:
            # Llamar al modelo para calcular
            subtotal, iva, total = CalculadoraImpuestos.calcular(
                valor_producto, cantidad, impuesto
            )

            # Devolver resultados en un diccionario (ideal para mostrar en vista)
            return {
                "subtotal": subtotal,
                "iva": iva,
                "total": total
            }

        except excepciones.ErrorPrecioNegativo as e:
            return {"error": str(e)}

        except excepciones.ErrorCantidadNegativa as e:
            return {"error": str(e)}

        except excepciones.ErrorPorcentajeImpuestoInvalido as e:
            return {"error": str(e)}

        except Exception as e:
            # Captura cualquier otro error inesperado
            return {"error": f"Error desconocido: {str(e)}"}
