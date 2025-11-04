from flask import Blueprint, render_template, redirect, url_for, flash

from web.models.ventas_repository import crear_tablas

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/init-db")
def init_db():
    """Opción en el menú para crear las tablas de la BD."""
    try:
        crear_tablas()
        flash("Tablas creadas / actualizadas correctamente.", "success")
    except Exception as exc:
        flash(f"Error al crear las tablas: {exc}", "error")
    return redirect(url_for("main.index"))
