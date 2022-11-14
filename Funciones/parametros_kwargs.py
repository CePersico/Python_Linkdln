# los argumentos seran de la forma diccionario {key: , value:----------- value---------}

def funcion_kwargs(**kwargs):
    print(kwargs)

# funcion_kwargs(nombre="Paco")

# cuando se ejecuta la funcion imprime:
# {'nombre': 'Paco'}


def funcion_kwargs_1(**kwargs):
    # print(kwargs)  {'nombre': 'Paco', 'apellido': 'Perez'}
    for llave, valor in kwargs.items():
        print(f"llave:{llave} valor:{valor}") # llave:apellido valor:Perez  llave:apellido valor:Perez
        print(kwargs["nombre"], kwargs["apellido"])  # Paco Perez
        print(kwargs["nombre"], kwargs["apellido"]) 
funcion_kwargs_1(nombre="Paco", apellido="Perez")

# al ejecutar se imprime:
# llave:nombre valor:Paco
# llave:apellido valor:Perez