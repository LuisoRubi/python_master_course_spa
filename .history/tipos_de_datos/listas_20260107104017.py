# lists 

colores = ["rojo", "azul", "verde"]

lista1 = [1, 3, 5, ["rojo", "azul", "negro"], "roberto", "jimenez"]

# print(lista1[2])

# busca el elemento dentro de la sublista
print("azul" in lista1[3])

# sintaxis para acceder a elementos de sublista
print(lista1[3][2])

# creo una lista en base a la indexación de la lista1 y después retorno la lista al revés
lista2 = lista1[3]
print(lista2[::-1])

# concateno una lista con la lista creada
print(lista1 + lista2 )

# las listas son objetos mutables
# lista1[3] = 3
# print(lista1)

# Agregar elementos en un alista con isnert es par aindiciar el indice o posicion donde se insteratara el elemento como aqui:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)