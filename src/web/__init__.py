from flask import Flask

from web.controllers.main import main_bp
from web.controllers.ventas import ventas_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev"  # en producción lee desde variables de entorno

    # Blueprints = capa de controladores (C del MVC)
    app.register_blueprint(main_bp)
    app.register_blueprint(ventas_bp, url_prefix="/ventas")

    return app
