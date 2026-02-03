# ============ Argumentos posicionales =============

# def mi_funcion(arg1, arg2, arg3):
#     print(arg1)
#     print(arg2)
#     print(arg3)

# mi_funcion("hey", "dude", "nice")
# Los argumentos que le proporcionamos e la invocacón de la función debe repetar el orden de los parámetros

# def mi_funcion2():
#     var = "var dentro de la función"
#     print(var)

# var = "var fuera de la función"
# mi_funcion2()
# print(var)

# En este caso particular, la var dentro de la función es diferente en memoria a la que está fuera, por el scope de las funciones


# ============ Argumentos keyword =============

# No es necesario respetar orden de los parámetros

# def mi_funcion3(arg1, arg2):
#     print(arg1)
#     print(arg2)

# var = "sup"
# var2 = "bro"

# mi_funcion3(arg1=var2, arg2=var)


# ============ Parámetros con valor por defecto =============

# Valor predefinido en los parámetreos de la función, siendo esto posible el poder llamar a la función con un número menor de argumentos
# No se puede poner un argumento con valor por defecto, antes de uno sin valor por defecto, da syntaxerror.
# Es un valor por defecto u opcional, es decir, si le indico un valor, lo reemplaza con el nuevo valor.

# def mi_funcion4(arg1, arg2="Mundo"):
#     print(arg1)
#     print(arg2)

# mi_funcion4("Hola")