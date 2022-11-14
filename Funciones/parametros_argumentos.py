# def calcular_area_cuadrado(lado):
#     """Calcular el area de un cuadrado"""
#     area = lado * lado
#     return area

# area_cuadrado = calcular_area_cuadrado(lado=5)
# print(area_cuadrado)

# def calcular_perimetro(lado1,lado2,lado3,lado4):
#     """Calcular el perimetro de un cuadrilatero"""
#     perimetro = lado1 + lado2 + lado3 + lado4
#     return perimetro

# perimetro_cuadrilatero = calcular_perimetro(1,2,3,4)
# print(perimetro_cuadrilatero)

def calcular_perimetro_args(*args):
    """Calcular el perimetro de una figura de n lados"""
    print(args)  # tupla: (1, 2, 3, 4, 5)
    perimetro = 0
    for lado in args:
        perimetro += lado
    return perimetro

perimetro_figura = calcular_perimetro_args(1,2,3, 4, 5)
print(perimetro_figura)