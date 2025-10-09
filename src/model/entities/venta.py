from datetime import datetime

class Venta:
    def __init__(self, venta_id, valor_unitario, cantidad, impuesto, subtotal, iva, total, created_at=None, updated_at=None):
        self.venta_id = venta_id
        self.valor_unitario = valor_unitario
        self.cantidad = cantidad
        self.impuesto = impuesto
        self.subtotal = subtotal
        self.iva = iva
        self.total = total
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def is_equal(self, other, tolerancia=1e-2):
        if not isinstance(other, Venta):
            return False
        return (
            abs(self.valor_unitario - other.valor_unitario) < tolerancia and
            self.cantidad == other.cantidad and
            abs(self.impuesto - other.impuesto) < tolerancia and
            abs(self.subtotal - other.subtotal) < tolerancia and
            abs(self.iva - other.iva) < tolerancia and
            abs(self.total - other.total) < tolerancia
        )
