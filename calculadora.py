
#paso 0: crear mi propia clase de excepción   

class ErrorPorcentajeImpuestoInvalido( Exception ):
    """Error cuando el impuesto es mayor a 100%"""

class ErrorPrecioNegativo( Exception):
    """Error cuando el valor del precio es negativo"""
    
class ErrorCantidadNegativa( Exception ):
    """Error caundo la cantidad de productos es negativa"""
    


def calcular(valor_producto, cantidad, impuesto):
    
    if valor_producto <= 0:
           raise ErrorPrecioNegativo ("Error: valor del producto inválido")
       
    
    if cantidad <= 0:
        raise ErrorCantidadNegativa ("Error: cantidad inválida")
    
    if impuesto < 0 or impuesto > 1:
        raise ErrorPorcentajeImpuestoInvalido("Error: impuesto inválido")
    
    

    return (valor_producto * cantidad) + ((valor_producto * cantidad) * impuesto)

    
        

def caso_1():
        
        #Entradas 
        valor_producto = 10_000
        cantidad = 5
        impuesto = 0.19
        
        #proceso
        calcular_impuesto = calcular(valor_producto,cantidad,impuesto)
        
        #verificar salida
        total_esperado = 59_500
        if total_esperado == calcular_impuesto:
            print("Prueba Normal 1 válida ")
        else:
            print("Prueba Normal 1 falló ")
        
        
def caso_2():
    
    #Entradas
    valor_producto = 5_000
    cantidad = 4
    impuesto = 0.19  
    
    #Proceso
    calcular_total = calcular(valor_producto, cantidad, impuesto)
    
    #Vérificar salida
    total_esperado = 23_800
    if calcular_total == total_esperado:
        print("Prueba Normal 2 válida")
    else:
        print("Prueba Normal 2 falló")
        

def caso_3():
    
    #Entrada
    valor_producto = 6_000
    cantidad = 3
    impuesto = 0.05  # IVA 5%
    
    #Proceso
    calcular_total = calcular(valor_producto, cantidad, impuesto)
    
    #Salida
    total_esperado = 18_900
    if calcular_total == total_esperado:
        print("Prueba Normal 3 válida")
    else:
        print("Prueba Normal 3 falló")
    

def caso_extraordinario_1():
    
    # Entradas
    valor_producto = 15_000
    cantidad = 2
    impuesto = 1.5  # 150%, inválido

    # Proceso
    resultado = calcular(valor_producto, cantidad, impuesto)

    # Salida esperada
    salida_esperada = "Error: impuesto inválido"
    if resultado == salida_esperada:
        print("Prueba Extraordinaria 1 válida")
    else:
        print("Prueba Extraordinaria 1 falló")


def caso_extraordinario_2():
    
    # Entradas
    valor_producto = 8_000
    cantidad = -3  # inválido
    impuesto = 0.19

    # Proceso
    resultado = calcular(valor_producto, cantidad, impuesto)

    # Salida esperada
    salida_esperada = "Error: cantidad inválida"
    if resultado == salida_esperada:
        print("Prueba Extraordinaria 2 válida")
    else:
        print("Prueba Extraordinaria 2 falló")
        

def caso_extraordinario_3():
        
    # Entradas
    valor_producto = 0  # inválido
    cantidad = 5
    impuesto = 0.05

    # Proceso
    resultado = calcular(valor_producto, cantidad, impuesto)

    # Salida esperada
    salida_esperada = "Error: valor del producto inválido"
    if resultado == salida_esperada:
        print("Prueba Extraordinaria 3 válida")
    else:
        print("Prueba Extraordinaria 3 falló")

