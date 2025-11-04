from decimal import Decimal, InvalidOperation

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)

from web.models.ventas_repository import (
    listar_ventas,
    crear_venta,
    obtener_venta,
    actualizar_venta,
)

ventas_bp = Blueprint("ventas", __name__)


@ventas_bp.route("/", methods=["GET"])
def listado():
    """Lista todas las ventas o busca por ID (?venta_id=)."""
    venta_id = request.args.get("venta_id", "").strip() or None
    ventas = listar_ventas(venta_id)
    return render_template("ventas_list.html", ventas=ventas, venta_id=venta_id)


@ventas_bp.route("/nueva", methods=["GET", "POST"])
def nueva():
    if request.method == "POST":
        return _guardar_venta()
    return render_template("ventas_form.html", venta=None, accion="crear")


@ventas_bp.route("/<int:venta_id>/editar", methods=["GET", "POST"])
def editar(venta_id: int):
    venta = obtener_venta(venta_id)
    if venta is None:
        flash(f"No existe la venta {venta_id}", "error")
        return redirect(url_for("ventas.listado"))

    if request.method == "POST":
        return _guardar_venta(venta_id=venta_id)

    return render_template("ventas_form.html", venta=venta, accion="editar")


def _guardar_venta(venta_id: int | None = None):
    """Lee datos del formulario, valida, calcula y guarda/actualiza."""
    try:
        valor_unitario = Decimal(request.form["valor_unitario"])
        cantidad = int(request.form["cantidad"])
        impuesto = Decimal(request.form["impuesto"])
    except (KeyError, InvalidOperation, ValueError):
        flash("Datos inválidos. Revisa valores numéricos.", "error")
        if venta_id is None:
            return redirect(url_for("ventas.nueva"))
        return redirect(url_for("ventas.editar", venta_id=venta_id))

    if valor_unitario <= 0 or cantidad <= 0 or impuesto < 0:
        flash("Valores no pueden ser negativos ni cero.", "error")
        if venta_id is None:
            return redirect(url_for("ventas.nueva"))
        return redirect(url_for("ventas.editar", venta_id=venta_id))

    if venta_id is None:
        crear_venta(valor_unitario, cantidad, impuesto)
        flash("Venta creada correctamente.", "success")
    else:
        actualizar_venta(venta_id, valor_unitario, cantidad, impuesto)
        flash("Venta actualizada correctamente.", "success")

    return redirect(url_for("ventas.listado"))
