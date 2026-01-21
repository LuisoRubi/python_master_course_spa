info_personal = {
    "Nombre": "Luis",
    "Apellido": "Mendoza",
    "Edad": "28",
    1: "atributo",
    ("uno", 1): "one"
    }

print(info_personal)

# se puede usar cualquier objeto inmutable como clave
# Recordar que la clave va en "" y los : van afuera de la clave o si no python pensará que el tipo de dato es un set
# otro fun fact es que por eso al imprimir el diccionario me salia desordenado cada vez, porque el interprete penso que creé un set y no un dict, los sets son desordenados

print(info_personal["Nombre"])
print(info_personal[1])
print(info_personal[("uno", 1)])

# Para agregar un nuevo elemento al diccionario solo basta con referenciar el nombre del diccionario y agregar el nuevo valor

info_personal["País"] = "México"
info_personal[("dos", 2)] = "two"
print(info_personal)

# En este caso sale str porque esta pidiendo el tipo del valor de la clave, no el tipo de la clave como tal
print(type(info_personal[("dos", 2)]))
# si quisiera saber el tipo de dato de la clave sería:
print(type(("dos", 2)))

# Si defino dos claves con el mismo nombre no me dara error pero si sobreescribirá el primer valor con el segundo

# Para agregar un nuevo item a un diccionario con cualqueir tipo de dato uso update

info_alumno = {}
print(info_alumno)
info_alumno.update({"nombre": "luis",
                    "edad": 23})
print(info_alumno)