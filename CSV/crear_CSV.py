import csv
import os

ruta = "csv_vacio_1.csv"
# si copiamos la tuta de la terminal es:
ruta_terminal = "C:\Users\Ana\Documents\PythonAvanzado\05_ARCHIVOS_CSV\csv_vacio_1.csv"
# pero notar que pone en otro color el 05, esto es porque no puede ponerse el nombre de una carpeta con inicio
# de numero, por lo que se debe cambiar \ por \ en cada lugar...y eso nos complica si es otro sistema operativo
ruta_absoluta = "C:\\Users\\Ana\\Documents\\PythonAvanzado\\05_ARCHIVOS_CSV\\csv_vacio_1.csv"
ruta_absoluta_os = os.path.join(os.getcwd(), "csv_vacio_1.csv")
# es mejor la ultima porque nos garanrtiza que sera correcta aunque usemos diferentes sistemas operativos
print(ruta_absoluta)
print(ruta_absoluta_os)

archivo_abierto = open(ruta_absoluta_os, "w")
writer = csv.writer(archivo_abierto, delimiter=",")
archivo_abierto.close()


# import csv
# ruta = "csv_vacio.csv"

# archivo_abierto = open(ruta, "w")
# writer = csv.writer(archivo_abierto, delimiter=",")
# archivo_abierto.close()
