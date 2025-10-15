from src.model.calculadora import CalculadoraImpuestos


class VentaController:
    """
    Controlador principal para gestionar las operaciones de la Calculadora de Impuestos de Ventas.
    Se encarga de orquestar la interacción entre la vista (interfaz) y el modelo (lógica de cálculo).
    """

    def __init__(self):
        # Inicializa el modelo de cálculo de impuestos
        self.calculadora = CalculadoraImpuestos()

    # -------------------------------------------------------------------------
    # MÉTODOS CRUD (Crear, Leer, Actualizar, Eliminar)
    # -------------------------------------------------------------------------

    def crear_venta(self, valor_unitario: float, cantidad: int, tipo_impuesto: str, porcentaje: float, exento: bool = False, excluido: bool = False) -> dict:
        """
        Crea una nueva venta y calcula los impuestos correspondientes.

        Parámetros:
            valor_unitario (float): Precio de una unidad del producto o servicio.
            cantidad (int): Cantidad de unidades vendidas.
            tipo_impuesto (str): Tipo de impuesto que aplica (IVA, INC, Licores...).
            porcentaje (float): Porcentaje del impuesto.
            exento (bool): Indica si el producto está exento del impuesto.
            excluido (bool): Indica si el producto está excluido del impuesto.

        Retorna:
            dict: Resultados del cálculo con subtotal, impuestos y total a pagar.
        """
        try:
            resultado = self.calculadora.calcular_total(
                valor_unitario=valor_unitario,
                cantidad=cantidad,
                tipo_impuesto=tipo_impuesto,
                porcentaje=porcentaje,
                exento=exento,
                excluido=excluido
            )
            return resultado
        except Exception as e:
            raise Exception(f"Error al crear la venta: {str(e)}")

    def consultar_venta(self, venta_id: int):
        """
        Consulta los datos de una venta específica (si se estuviera guardando en memoria o base de datos).
        En esta versión no persistente, este método puede ser opcional.
        """
        raise NotImplementedError("Función de consulta no implementada. Esta versión no guarda datos.")

    def modificar_venta(self, venta_id: int, nuevos_datos: dict):
        """
        Modifica los datos de una venta existente.
        En esta versión no persistente, este método puede ser opcional.
        """
        raise NotImplementedError("Función de modificación no implementada. Esta versión no guarda datos.")

    def eliminar_venta(self, venta_id: int):
        """
        Elimina una venta (si se estuviera almacenando en una base de datos o lista).
        """
        raise NotImplementedError("Función de eliminación no implementada. Esta versión no guarda datos.")

    # -------------------------------------------------------------------------
    # MÉTODOS AUXILIARES
    # -------------------------------------------------------------------------

    def calcular_iva(self, valor: float, porcentaje: float) -> float:
        """Calcula el IVA de un valor dado."""
        return round(valor * (porcentaje / 100), 2)

    def calcular_inc(self, valor: float, porcentaje: float) -> float:
        """Calcula el Impuesto Nacional al Consumo (INC)."""
        return round(valor * (porcentaje / 100), 2)

    def calcular_licores(self, valor: float, grados_alcohol: float) -> float:
        """
        Calcula el impuesto sobre licores basado en la tarifa de ejemplo:
        $150 por grado de alcohol/litro + 20% del valor de venta.
        """
        return round((150 * grados_alcohol) + (valor * 0.20), 2)
