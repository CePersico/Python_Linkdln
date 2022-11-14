"""Desde el shell de Python
lambda num: num * 2
_(2,)
(lambda num: num * 2)(2)
multiplicacion = lambda num: num * 2
multiplicacion(2)
"""


# Las funciones lambda las podemos usar para evaluar o calcular expresiones cortas, siempre deben poder definirse en una unica linea


# La funcion separar_par_impar no  puede transformarse en una funcion anonima(lambda) ya que tiene varias instrucciones

# def separar_par_impar(lista_numeros):
#     pares = []
#     impares = []
#     for numero in lista_numeros:
#         if numero %2 == 0:
#             pares.append(numero)
#         else:
#             impares.append(numero)
#     return pares, impares

# La funcion calcular_area_cuadrado puede transformarse en una funcion anonima(lambda) ya que tiene una instruccion sencilla

# def calcular_area_cuadrado(lado):
#     return lado ** 2

# Expresion de la misma funcion como anonima:

# calcular_cuadrado = lambda lado: lado ** 2
# print(calcular_cuadrado(2))


lista_numeros = [1,2,3,4,5,6,7,8]

lista_bool = lambda numero: numero % 2 == 0
print (lista_bool(4)) # true

lista_pares = list(filter(lambda numero: numero % 2 == 0, lista_numeros))
print(lista_pares)

nueva_lista = list(map(lambda numero: numero * 10, lista_numeros))
print(nueva_lista)