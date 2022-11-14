import csv

##############################
# with open("datos.csv", "r", encoding="UTF-8") as archivo:
#     si le dejo el: encoding="UTF-8".. mde tira error!!
##############################

# with open("datos.csv", "r") as archivo:
#     reader = csv.reader(archivo)
#     for fila in reader:
#         print(fila)
# ['nombre', 'apellido', 'edad']
# ['Paco', 'Botero', '21']
# ['Javier', 'Quiñonez', '23']
# ['Emilio', 'Tafur', '20']

# with open("datos.csv", "r") as archivo:
#     reader = csv.reader(archivo)
#     next(reader) # asi evitamos escribir la primer linea
#     print("Columnas", next(reader))
#     for fila in reader:
#         print(fila)
# ['Paco', 'Botero', '21']
# ['Javier', 'Quiñonez', '23']
# ['Emilio', 'Tafur', '20']

# podemos leer solo algun elemento de cada fila:
# with open("datos.csv", "r") as archivo:
#     reader = csv.reader(archivo)
#     next(reader) # asi evitamos escribir la primer linea
#     for fila in reader:
#         print(fila[0])
# Paco
# Javier
# Emilio


# con diccionario:
# with open("datos.csv", "r") as archivo:
#     reader = csv.DictReader(archivo)
#     for fila in reader:
#         print(fila)
# {'nombre': 'Paco', 'apellido': 'Botero', 'edad': '21'}
# {'nombre': 'Javier', 'apellido': 'Quiñonez', 'edad': '23'}
# {'nombre': 'Emilio', 'apellido': 'Tafur', 'edad': '20'}


with open("datos.csv", "r") as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        print(fila["nombre"])
# Paco
# Javier
# Emilio