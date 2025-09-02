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

CALCULADORAIMPUESTOSVENTAS/
│
├── src/ # Código fuente de la lógica de la aplicación
│ ├── controller/ # Lógica de control (conexión entre modelo y vista)
│ │ └── init.py
│ │
│ ├── model/ # Capa de lógica del negocio
│ │ ├── init.py
│ │ └── calculadora.py # Lógica principal del cálculo de impuestos
│ │
│ ├── view/ # Capa de presentación o interfaz con el usuario
│ │ ├── init.py
│ │ └── interfaz.py # Interfaz de usuario (ej. menú en consola)
│
├── test/ # Pruebas unitarias
│ ├── init.py
│ └── test.py # Pruebas para validar cálculos y errores
│
├── Casos.xlsx # Archivo Excel con casos de prueba o ejemplos de uso
├── .gitignore # Ignora archivos/carpeta innecesarios para Git
└── README.md # Documentación del proyecto



## ¿Cómo lo hago funcionar?

### Prerrequisitos
- Tener instalado **Python 3.10+**.  
- Clonar este repositorio en tu máquina local.  

### Ejecución (fuera del entorno de desarrollo)
Ubicados en la carpeta raíz del proyecto `CalculadoraImpuestosVentas`, ejecute el siguiente comando en la terminal para abrir la interfaz de consola:

```bash
python src/view/interfaz.py


```
## ¿Cómo ejecuto las pruebas unitarias?

Las pruebas unitarias garantizan que:  
- El cálculo del **subtotal, IVA y total** sea correcto en diferentes escenarios.  
- Las **excepciones personalizadas** funcionen correctamente:  
  - `ErrorPrecioNegativo`  
  - `ErrorCantidadNegativa`  
  - `ErrorPorcentajeImpuestoInvalido`  

### Pasos para ejecutar las pruebas unitarias:

1. Abre una terminal en la **carpeta raíz** del proyecto (`CalculadoraImpuestosVentas`).  

2. Ejecuta el siguiente comando para recorrer toda la carpeta `test/` y correr **todas las pruebas**:  

```bash
python -m unittest discover -s test -p "test*.py"

