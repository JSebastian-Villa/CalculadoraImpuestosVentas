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
## Estructura

```plaintext
CALCULADORAIMPUESTOSVENTAS/ 
├── src/                 # Código fuente de la lógica de la aplicación 
│   ├── controller/      # Lógica de control (conexión entre modelo y vista) 
│   │   └── __init__.py
│   ├── model/           # Capa de lógica del negocio 
│   │   ├── __init__.py
│   │   └── calculadora.py # Lógica principal del cálculo de impuestos 
│   ├── view/            # Capa de presentación o interfaz con el usuario (ej. menú en consola) 
│       ├── __init__.py
│       └── interfaz.py
├── test/                # Pruebas unitarias 
│   ├── __init__.py
│   └── test.py          # Pruebas para validar cálculos y errores 
├── Casos.xlsx           # Archivo Excel con casos de prueba o ejemplos de uso 
├── .gitignore           # Ignora archivos/carpeta innecesarios para Git 
└── README.md            # Documentación del proyecto



## ¿Cómo lo hago funcionar?

### Prerrequisitos
- Tener instalado **Python 3.10+**.
- Haber **clonado** este repositorio en tu computador.

### Ejecución (fuera del entorno de desarrollo)
Sigue estos pasos tal cual:

1. **Abre una terminal**:
   - Windows: abre *PowerShell* o *CMD*.
   - macOS/Linux: abre *Terminal*.

2. **Ve a la carpeta del proyecto** (la raíz donde ves `src/` y `test/`):
   - Ejemplo Windows:
     ```bash
     cd C:\Users\TuUsuario\Documents\CalculadoraImpuestosVentas
     ```
   - Ejemplo macOS/Linux:
     ```bash
     cd ~/Documents/CalculadoraImpuestosVentas
     ```

3. **Ejecuta la interfaz de consola**:
   - Con `python` (la mayoría de sistemas):
     ```bash
     python src/view/interfaz.py
     ```
   - Si tu sistema usa `python3`:
     ```bash
     python3 src/view/interfaz.py
     ```

4. **Ingresa los datos cuando te los pida**:
   - Valor del producto (ej: `10000`)
   - Cantidad (ej: `5`)
   - Impuesto en **porcentaje** (ej: `19` para 19%)

5. **Lee el resultado en pantalla**:
   - Verás **Subtotal**, **IVA** y **Total a pagar** formateados.

> *Si aparece* `ModuleNotFoundError: No module named 'model'` o `No module named 'src'`, asegúrate de:
> - Estar **parado en la raíz del proyecto** (paso 2).
> - Ejecutar **exactamente** el comando del paso 3 (respetando mayúsculas/minúsculas y rutas).


## ¿Cómo ejecuto las pruebas unitarias?

Las pruebas unitarias garantizan que:
- El cálculo del **subtotal, IVA y total** sea correcto en diferentes escenarios.
- Las **excepciones personalizadas** funcionen correctamente:
  - `ErrorPrecioNegativo`
  - `ErrorCantidadNegativa`
  - `ErrorPorcentajeImpuestoInvalido`

### Pasos para ejecutar las pruebas unitarias

1. **Abre una terminal** (PowerShell/CMD en Windows, Terminal en macOS/Linux).

2. **Ve a la carpeta raíz del proyecto**:
   - Windows:
     ```bash
     cd C:\Users\TuUsuario\Documents\CalculadoraImpuestosVentas
     ```
   - macOS/Linux:
     ```bash
     cd ~/Documents/CalculadoraImpuestosVentas
     ```

3. **Ejecuta el archivo de pruebas por ruta (como pides, sin atajos)**:
   - Con `python`:
     ```bash
     python -m unittest test/test.py
     ```
   - Si tu sistema usa `python3`:
     ```bash
     python3 -m unittest test/test.py
     ```

4. **Revisa el resultado**:
   - Si todo está bien, verás algo similar a:
     ```
     .........
     ----------------------------------------------------------------------
     Ran 9 tests in 0.00Xs

     OK
     ```

> **Opcional:** Para ejecutar *todas* las pruebas que haya en la carpeta `test/` (si más adelante agregas más archivos):
> ```bash
> python -m unittest discover -s test -p "test*.py"
> ```
> (Usa `python3` si tu sistema lo requiere).

