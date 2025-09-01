# CalculadoraImpuestosVentas

## ¿Qué hace esta calculadora?

Esta calculadora permite obtener el total a pagar por la venta de un producto o servicio en Colombia, considerando diferentes impuestos que pueden aplicar, según el tipo de bien o servicio. Es útil para comercios, facturadores electrónicos, contadores y desarrolladores de software.

## Autores
Escrito por:
- Juan Esteban Echavarría
- Juan Sebastián Villa 

## ¿Qué impuestos calcula?

1. **IVA (Impuesto al Valor Agregado)**  
   - Tasa estándar del **19%**, pero puede ser **0%** si está exento o excluido.
   - Aplica a la mayoría de los bienes y servicios, excepto productos básicos (exentos) o no gravados (excluidos).

2. **INC (Impuesto Nacional al Consumo)**  
   - Aplica a restaurantes, bares, bebidas azucaradas y algunos servicios.
   - Generalmente del **8%**.

3. **Impuesto de Rentas a los Licores**  
   - Impuesto especial para licores, vinos y aperitivos.
   - Depende del volumen de alcohol y valor del producto. Puede calcularse como un porcentaje fijo más una tarifa por grado de alcohol.
   - Ejemplo: **$150 por grado alcohol/litro + 20% sobre el precio de venta**.


## Entradas
- El valor unitaario del producto.
- La cantidad de unidades a vender.
- El tipo de impuesto que aplica.
- El porcentaje correspondiente al impuesto.
- Si el producto esta exento o excluido de algun impuesto.

## Salidas
- El subtotal (precio unitario multiplicado por la cantidad.
- El valor del IVA calculado (si aplica).
- El valor del INC (si aplica).
- El impuesto adicional si se trata de licores.
- El valor total a pagar sumando todos los impuestos aplicados.
  

Link del audio de la entrevista: https://soundcloud.com/sebastian-villa-946690590/audio-entrevista

---

## 🧪 Instrucciones para ejecutar las pruebas unitarias

El proyecto incluye un conjunto de pruebas unitarias ubicadas en la carpeta `test/`.  
Estas pruebas validan:

- Que las excepciones personalizadas funcionen correctamente (`ErrorPrecioNegativo`, `ErrorCantidadNegativa`, `ErrorPorcentajeImpuestoInvalido`).  
- Que el cálculo de subtotal, IVA y total se realice correctamente en casos normales.  

### Pasos para ejecutar las pruebas:
1. Abre una terminal en la raíz del proyecto (`CalculadoraImpuestosVentas`).  
2. Ejecuta el siguiente comando para correr **todas las pruebas**:

   ```bash
   python -m unittest discover -s test -p "test*.py"
