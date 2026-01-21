info_personal = {
    "Nombre": "Luis",
    "Apellido": "Mendoza",
    "Edad": "28",
    1: "atributo"
    }

print(info_personal)

# se puede usar cualquier objeto inmutable como clave
# Recordar que la clave va en "" y los : van afuera de la clave o si no python pensará que el tipo de dato es un set

print(info_personal["Nombre"])
print(info_personal[1])