import json

persona = {
    "nombre": "Javier",
    "apellido": "Quinonez",
    "edad": 24
}
# para serializar se usa la funcion dumps()  
# objeto_json = json.dumps(persona, indent=2)
# # sentencia with y funcion open():
# with open("persona.json", "w") as archivo_json:  # 'w': write
#     archivo_json.write(objeto_json)
    # json.dump(persona, archivo_json)
# de otra forma:
    # objeto_json = json.dumps(persona, indent=2)

# sentencia with y funcion open():
with open("persona.json", "w") as archivo_json:  # 'w': write
    json.dump(persona, archivo_json)