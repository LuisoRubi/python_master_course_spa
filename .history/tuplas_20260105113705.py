tupla = (1, 2, 3, 4)
print(tupla)

# las tubplas son objeto sinmutables, es bueno para proyectos escalables, más rápidas también

# Asignar un solo elemento numpérico en una tupla puede ser confuso par apython ya que lo va a marcar como int
tupla1 = (4)
print(type(tupla1))
# a nivel de sintaxis, la forma en la que podemos definirla tupla así sería:
tupla1 = (4,)
print(type(tupla1))

# packing y unpacking de tuplas
colores = ("azul", "amarillo", "rojo")
color1, color2, color3 = colores
print(color1)
print(color2)
print(color3)

# podemos usar tuplas para devovler mpultiples valores

def func():
    return (4, 2)

print(val1, val2 = func())

