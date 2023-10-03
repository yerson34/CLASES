#Crea una funcion por cada operador artmetrico
#  y que revida 2 paramatros y retorna el resultado de la operacion, ojo 
# . crease un funcion que nos permite imprimir el resultado
# 1. Función de suma:

def suma(a, b):
    resultado = a + b
    return resultado

def imprimir_resultado(resultado):
    print("El resultado es:", resultado)


# 2. Función de resta:

def resta(a, b):
    resultado = a - b
    return resultado

def imprimir_resultado(resultado):
    print("El resultado es:", resultado)


# 3. Función de multiplicación:

def multiplicacion(a, b):
    resultado = a * b
    return resultado

def imprimir_resultado(resultado):
    print("El resultado es:", resultado)


#4. Función de división:

def division(a, b):
    resultado = a / b
    return resultado

def imprimir_resultado(resultado):
    print("El resultado es:", resultado)
#6-. escribir una funcion que reciba un numero entero positivo y devuelvesu factorial
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# 7-. escribir  una funcion fue resiva como parametros una lista de numeros y reterne una nueva lista con el cuadro de cada numero de la lista ingresada

def calcular_cuadrados(lista):
    cuadrados = []
    for num in lista:
        cuadrados.append(num ** 2)
    return cuadrados
    #8-.escribir un programa que reciba una cadena de caracteres y devuelva un objeto con cada palabra que contiene y su frecuencia
def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia

cadena = input("Ingresa una cadena de caracteres: ")
resultado = contar_palabras(cadena)
print(resultado)
