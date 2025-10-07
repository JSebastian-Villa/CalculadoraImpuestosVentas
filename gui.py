import sys
sys.path.append("src")
from src.view.gui.interfaz_grafica import CalculadoraCompras

if __name__ == "__main__":
    app = CalculadoraCompras()
    app.run()
