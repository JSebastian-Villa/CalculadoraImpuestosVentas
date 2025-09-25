from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.graphics import Color, Rectangle

import sys
sys.path.append("src")
from model import calculadora
from model import excepciones


class CalculadoraCompras(App):

    def build(self):

        self.color_fondo = [245/255, 245/255, 245/255, 1]
        self.color_texto = [51/255, 51/255, 51/255, 1]
        self.color_boton = [59/255, 130/255, 246/255, 1]
        self.color_boton_cerrar = [239/255, 68/255, 68/255, 1]

        contenedor = BoxLayout(orientation="vertical", padding=20, spacing=15)

        with contenedor.canvas.before:
            Color(*self.color_fondo)
            self.rect = Rectangle(size=contenedor.size, pos=contenedor.pos)
        contenedor.bind(size=self._update_rect, pos=self._update_rect)

        fila_valor = BoxLayout(orientation="horizontal", spacing=10)
        etiqueta_valor = Label(text="Valor unitario del producto", color=self.color_texto)
        self.valor_producto = TextInput(multiline=False,
                                        background_color=[1, 1, 1, 1],
                                        foreground_color=self.color_texto)
        fila_valor.add_widget(etiqueta_valor)
        fila_valor.add_widget(self.valor_producto)
        contenedor.add_widget(fila_valor)

        fila_cantidad = BoxLayout(orientation="horizontal", spacing=10)
        etiqueta_cantidad = Label(text="Cantidad de productos", color=self.color_texto)
        self.cantidad = TextInput(multiline=False,
                                  background_color=[1, 1, 1, 1],
                                  foreground_color=self.color_texto)
        fila_cantidad.add_widget(etiqueta_cantidad)
        fila_cantidad.add_widget(self.cantidad)
        contenedor.add_widget(fila_cantidad)


        fila_impuesto = BoxLayout(orientation="horizontal", spacing=10)
        etiqueta_impuesto = Label(text="Impuesto", color=self.color_texto)

        self.dropdown = DropDown()
        impuestos = {
            "IVA (19%)": 0.19,
            "Reducido (5%)": 0.05,
            "Exento (0%)": 0.0,
            "Manual": None
        }

        self.impuesto_valor = None  
        self.manual_input = None

        self.mainbutton = Button(text="Seleccionar impuestos", size_hint_y=None, height=44)
        self.mainbutton.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: self.seleccionar_impuesto(x))

        
        for nombre, valor in impuestos.items():
            btn = Button(text=nombre, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)

        fila_impuesto.add_widget(etiqueta_impuesto)
        fila_impuesto.add_widget(self.mainbutton)
        contenedor.add_widget(fila_impuesto)

        boton_calcular = Button(text="Calcular",
                                background_normal="",
                                background_color=self.color_boton,
                                color=[1, 1, 1, 1],
                                size_hint=(1, None), height=50)
        boton_calcular.bind(on_press=self.calcular_compra)
        contenedor.add_widget(boton_calcular)

        boton_limpiar = Button(text="Limpiar",
                       background_normal="",
                       background_color=[156/255, 163/255, 175/255, 1],  # gris
                       color=[1, 1, 1, 1],
                       size_hint=(1, None), height=40)
        boton_limpiar.bind(on_press=self.limpiar_campos)
        contenedor.add_widget(boton_limpiar)

        self.subtotal_label = Label(text="Subtotal: ", color=self.color_texto)
        contenedor.add_widget(self.subtotal_label)

        self.impuesto_label = Label(text="Impuesto: ", color=self.color_texto)
        contenedor.add_widget(self.impuesto_label)

        self.total_label = Label(text="Total: ", color=self.color_texto)
        contenedor.add_widget(self.total_label)

        return contenedor

    def seleccionar_impuesto(self, seleccion):
        self.mainbutton.text = seleccion

        if seleccion == "IVA (19%)":
            self.impuesto_valor = 0.19
            self.manual_input = None
        elif seleccion == "Reducido (5%)":
            self.impuesto_valor = 0.05
            self.manual_input = None
        elif seleccion == "Exento (0%)":
            self.impuesto_valor = 0.0
            self.manual_input = None
        elif seleccion == "Manual":
            contenido = BoxLayout(orientation="vertical", padding=15, spacing=10)
            self.manual_input = TextInput(hint_text="Ingrese impuesto (ej: 0.15)", multiline=False)
            boton_ok = Button(text="Aceptar", size_hint=(1, None), height=40,
                              background_normal="", background_color=self.color_boton,
                              color=[1, 1, 1, 1])

            contenido.add_widget(self.manual_input)
            contenido.add_widget(boton_ok)

            popup = Popup(title="Impuesto manual",
                          content=contenido,
                          size_hint=(0.7, 0.4),
                          auto_dismiss=False)

            boton_ok.bind(on_press=lambda x: self._guardar_manual(popup))
            popup.open()

    def _guardar_manual(self, popup):
        try:
            self.impuesto_valor = float(self.manual_input.text)
            popup.dismiss()
        except ValueError:
            self.manual_input.text = ""

    def limpiar_campos(self, sender):
        self.valor_producto.text = ""
        self.cantidad.text = ""
        self.mainbutton.text = "IVA (19%)"
        self.impuesto_valor = 0.19
        self.subtotal_label.text = "Subtotal: "
        self.impuesto_label.text = "Impuesto: "
        self.total_label.text = "Total: "

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def calcular_compra(self, sender):
        try:
            valor = float(self.valor_producto.text)
            cantidad = int(self.cantidad.text)
            impuesto = float(self.impuesto_valor)

            subtotal, iva, total = calculadora.calcular(valor, cantidad, impuesto)

            self.subtotal_label.text = f"Subtotal: {subtotal:.2f}"
            self.impuesto_label.text = f"Impuesto: {iva:.2f}"
            self.total_label.text = f"Total: {total:.2f}"

        except (ValueError, excepciones.ErrorPrecioNegativo,
                excepciones.ErrorCantidadNegativa,
                excepciones.ErrorPorcentajeImpuestoInvalido) as e:

            contenido = BoxLayout(orientation="vertical", padding=15, spacing=10)
            mensaje = Label(text=str(e), color=[1, 1, 1, 1])
            boton_cerrar = Button(text="Cerrar", size_hint=(1, None), height=40,
                                  background_normal="", background_color=self.color_boton_cerrar,
                                  color=[1, 1, 1, 1])

            contenido.add_widget(mensaje)
            contenido.add_widget(boton_cerrar)

            popup = Popup(title="Error en los datos",
                          content=contenido,
                          size_hint=(0.7, 0.4),
                          auto_dismiss=False)

            boton_cerrar.bind(on_press=popup.dismiss)
            popup.open()


if __name__ == "__main__":
    app = CalculadoraCompras()
    app.run()