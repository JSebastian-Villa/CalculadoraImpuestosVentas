# CalculadoraImpuestosVentas

## ¿Qué hace esta calculadora?

Esta calculadora permite obtener el total a pagar por la venta de un producto o servicio en Colombia, considerando diferentes impuestos que pueden aplicar, según el tipo de bien o servicio. Es útil para comercios, facturadores electrónicos, contadores y desarrolladores de software.

## Autores
Escrito por:
- Juan Esteban Echavarría
- Juan Sebastián Villa

## Autores Interfaz Grafica
- Jhon Fredy Asprilla Aguilar
- Julián David Osorio Londoño

## Ejecución de la interfaz gráfica

Para ejecutar la calculadora de Hipoteca Inversa con Kivy, asegúrate de tener instaladas las dependencias necesarias (principalmente **Kivy**).  

1. Clona este repositorio o descarga los archivos.  
2. Abre una terminal en la carpeta del proyecto.  
3. Ejecuta el siguiente comando:


python src\view\GUI Interfaz_Grafica

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
- El subtotal (precio unitario multiplicado por la cantidad).
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
│   └── view/            # Capa de presentación o interfaz con el usuario (ej. menú en consola)
|       ├── Console/
│       |   ├── __init__.py
│       |   └── interfaz.py
|       └── Gui/
|           └─ interfaz_grafica.py # Interfaz Grafica 
├── test/                # Pruebas unitarias 
│   ├── __init__.py
│   └── test.py          # Pruebas para validar cálculos y errores 
├── Casos.xlsx           # Archivo Excel con casos de prueba o ejemplos de uso 
├── .gitignore           # Ignora archivos/carpeta innecesarios para Git 
└── README.md            # Documentación del proyecto
```


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


# Instrucciones para crear la base de datos, realizar la conexión y ejecutar el programa

---

## 1️ Crear la base de datos

Ejecutar los siguientes comandos en **PostgreSQL**:

```sql
CREATE DATABASE calculadora_impuestos;

CREATE TABLE IF NOT EXISTS ventas (
  venta_id SERIAL PRIMARY KEY,
  valor_unitario NUMERIC(12,2) NOT NULL,
  cantidad INT NOT NULL,
  impuesto NUMERIC(6,4) NOT NULL,
  subtotal NUMERIC(14,2) NOT NULL,
  iva NUMERIC(14,2) NOT NULL,
  total NUMERIC(14,2) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);sql
```
## 2️⃣ Crear el archivo `.env`

 **Ubicación:** carpeta raíz del proyecto

```
DB_NAME=calculadora_impuestos
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432

Importante: Este archivo contiene credenciales privadas.
```
## 3️⃣ Crear el archivo `secret_config.py`

 **Ubicación:** `src/secret_config.py`

Este archivo permite leer las variables del archivo `.env` sin exponer datos privados.

```python
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    dbname: str = os.getenv("DB_NAME", "")
    user: str = os.getenv("DB_USER", "")
    password: str = os.getenv("DB_PASSWORD", "")
    host: str = os.getenv("DB_HOST", "")
    port: str = os.getenv("DB_PORT", "5432")

settings = Settings()
```
## 4️⃣ Configurar la conexión a la base de datos

 **Ubicación:** `src/model/conexion_db.py`

Este archivo establece la conexión con la base de datos PostgreSQL utilizando las variables de entorno definidas en `secret_config.py`.

```python
import psycopg2
from src.secret_config import settings

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname=settings.dbname,
            user=settings.user,
            password=settings.password,
            host=settings.host,
            port=settings.port
        )
        print("✅ Conexión exitosa a la base de datos")
        return conn
    except Exception as e:
        print(" Error al conectar con la base de datos:", e)
        return None
```
## 5️⃣ Ejecución del programa

### 🔹 Activar el entorno virtual

**En Windows:**
```bash
.venv\Scripts\activate

**En macOS/Linux:**
source .venv/bin/activate

**Ejecutar la interfaz de consola**
python src/view/Console/interfaz.py

**Ejecutar la interfaz gráfica**
python src/view/GUI/interfaz_grafica.py
```
## ✅ Pruebas unitarias

Las pruebas validan:

- Cálculo correcto de **subtotal**, **IVA** y **total**.  
- Manejo adecuado de **excepciones personalizadas**.  
- Funcionalidad **CRUD** de la base de datos.

---

###  Ejecutar las pruebas

```bash
python -m unittest discover -s test -p "test*.py"

.........
----------------------------------------------------------------------
Ran 9 tests in 0.00Xs

OK


#  Calculadora de Impuestos de Ventas

Aplicación web desarrollada en Python y Flask para calcular impuestos de ventas.

##  Acceso en línea

Puedes acceder a la aplicación desde el siguiente enlace:

https://calculadoraimpuestosventas-2.onrender.com


