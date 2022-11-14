import csv

columnas = ["nombre", "apellido", "edad"]
dato_1 = ["Paco", "Botero", 26]
dato_2 = ["Javier", "Quiñonez", 24]
dato_3 = ["Emilio", "Tafur", 25]

datos_lista = [
    ["Paco", "Botero", 26],
    ["Javier", "Quiñonez", 24],
    ["Emilio", "Tafur", 25]
]
datos_dict = [
    {"nombre": "Paco", "apellido": "Botero", "edad": 21},
    {"nombre": "Javier", "apellido": "Quiñonez", "edad": 23},
    {"nombre": "Emilio", "apellido": "Tafur", "edad": 20}
]

# archivo = open("datos.csv","w")
# writer = csv.writer(archivo, delimiter=",")
# archivo.close()


# with open("datos.csv", "w") as archivo:
#     writer = csv.writer(archivo, delimiter=",")
#     writer.writerow(columnas)
#     writer.writerow(dato_1)
#     writer.writerow(dato_2)
#     writer.writerow(dato_3)
    # con estas lineas el archivo dato queda:
    # nombre,apellido,edad

    # Paco,Botero,26

    # Javier,Qui�onez,24

    # Emilio,Tafur,25
# para evitrar los saltos de linea vacion en el medio hay que agregar
# with open("datos.csv", "w", newline = "") as archivo:
#     writer = csv.writer(archivo, delimiter=",")
#     writer.writerow(columnas)
#     writer.writerow(dato_1)
#     writer.writerow(dato_2)
#     writer.writerow(dato_3)
    # ahora queda: nombre,apellido,edad
# Paco,Botero,26
# Javier,Qui�onez,24
# Emilio,Tafur,25

# es mas rapido hacer:
# with open("datos.csv", "w", newline = "") as archivo:
#     writer = csv.writer(archivo, delimiter=",")
#     writer.writerow(columnas)
#     writer.writerows(datos_lista)
# nombre,apellido,edad
# Paco,Botero,26
# Javier,Qui�onez,24
# Emilio,Tafur,25

# si usamos diccionarios:
with open("datos.csv", "w", newline = "") as archivo:
    writer = csv.DictWriter(archivo, fieldnames=columnas)
    writer.writeheader() # para que se escriba la primera fila con los nombres de las columnas
    writer.writerows(datos_dict)