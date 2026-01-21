# Un set no se puede indexar, no respetan un orden y no puede contener valores duplicados
myset = {"rojo", "azul", "verde"}
print(type(myset))

# muy util para eliminar valores duplicados de la slistas y tuplas

lista = ["rojo", "verde", "azul", "naranja", "rojo", "azul"]
lista_no_repeat = set(lista)

print(lista_no_repeat)