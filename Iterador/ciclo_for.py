"""
Ciclo for en otros lenguajes
for (inicializador; condición; iterador) {
    instrucción
}
Ciclo for en JS
let nombres = ["Paco", "Emilio", "Javier"]
for (let i = 0; i < nombres.length; i += 1){
    console.log(nombres[i])
}
Ciclo for en Python
for elemento in list:
    instruccion

Iteradores en Python:
iter(): permite recorrer el iterable y 
next(): retorna el elemento siguiente en el iterable
""" 

#  for:

# nombres = ["Paco", "Emilio", "Javier"]
# for elemento in nombres:
#     print(elemento)

# Paco
# Emilio
# Javier

# break_continue:  break: detiene el ciclo
# nombres = ["Paco", "Emilio", "Javier"]

# for elemento in nombres:
#     if elemento[0] == 'E':
#         break
#     print(elemento)  # Paco


# for elemento in nombres:
#     if elemento[0] == 'E':
#         continue  # cuando se cumple la condicion se le pide al ciclo 
#     # que continue con la siguiente iteracion, por lo que se salteo a 
#     # Emilo en el print
#     print(elemento)  
# Paco
# Javier

# for elemento in nombres:
    # print(elemento)  # Paco
    # break # Rompe con el ciclo por lo que imprime solo el primero de la lista
    
# for elemento in nombres:
#     print(elemento)
#     continue  #Imprime toda la lista

    
# for elemento in nombres:
#     continue     # no imprime nada
#     print(elemento)  # solo itera por cada elemento de la lista sin ejecutrar la sentencia print
   


# range:


"""
range(inicio, fin, paso)
"""
# serie_1 = range(5)
# print(list(serie_1)) # [0, 1, 2, 3, 4]

# serie_2 = range(5,10)
# print(list(serie_2))  # [5, 6, 7, 8, 9]

# serie_3 = range(3,10,2)
# print(list(serie_3)) # [3, 5, 7, 9]

# for elemento in serie_3:
#     print(elemento)

#  zip
nombres = ["Paco", "Emilio", "Javier", "Ana"]
# #posicion:     0      1         2        3  
apellidos = ["Botero", "Tafur", "Quiñonez"]
# #posicion:     0         1         2          
# nombre_completo = list(zip(nombres, apellidos))
# print(nombre_completo)
# observar que como falta un a apellido no pone aq Ana en la lista zip
# [('Paco', 'Botero'), ('Emilio', 'Tafur'), ('Javier', 'Quiñonez')]

# unzip es desempaquetar una lista:
# nombres_unZip, apellidos_unzip = zip(*nombre_completo)
# print(nombres_unZip)
# print(apellidos_unzip)
# ('Paco', 'Emilio', 'Javier')
# ('Botero', 'Tafur', 'Quiñonez')

# for nombre, apellido in zip(nombres, apellidos):
#     print(nombre, apellido)
# Paco Botero
# Emilio Tafur
# Javier Quiñonez
"""
enumerate(objeto iterable, start=0)
"""

# nombres = ["Paco", "Emilio", "Javier", "Ana"]
# nombres_enumerados = enumerate(nombres, start=5) # por defecto inicia en 0
# print(list(nombres_enumerados))
# tupla: [(5, 'Paco'), (6, 'Emilio'), (7, 'Javier'), (8, 'Ana')]

# for indice, elemento in enumerate(nombres):
#     print(indice, elemento)
# 0 Paco
# 1 Emilio
# 2 Javier
# 3 Ana

# for_else:

lista_nombres = ["Paco", "Emilio", "Javier", "Ana"]

for nombre in lista_nombres:
    print(nombre)
    # if nombre == "Javier":
    #     break
else:
    print("Ciclo terminado")

# Paco
# Emilio
# Javier
# Ciclo terminado


for nombre in lista_nombres:
    print(nombre)
    if nombre == "Javier":
        break
else:
    print("Ciclo terminado")  # aca no entra porque se rompio el ciclo

# Paco
# Emilio
# Javier