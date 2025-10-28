from flask import Flask, render_template, request
import sys
sys.path.append("src")
from model.calculadora import CalculadoraImpuestos

app = Flask(__name__)

@app.route("/")

def hello_world():
    return render_template("calc_impuesto.html")

@app.route("/calculadora")
def calcular_ruta():
    valor_producto = float(request.args["valor_producto"])
    cantidad = float(request.args["cantidad"])
    impuesto = float(request.args["impuesto"])

    valor_total = CalculadoraImpuestos.calcular( valor_producto, cantidad, impuesto)
    return f"El valor de la compra es: {valor_total}"

app.run(debug=True)
                     
