# ============ Argumentos posicionales =============

# def mi_funcion(arg1, arg2, arg3):
#     print(arg1)
#     print(arg2)
#     print(arg3)

# mi_funcion("hey", "dude", "nice")
# Los argumentos que le proporcionamos e la invocacón de la función debe repetar el orden de los parámetros




def mi_funcion2():
    var = "var dentro de la función"
    print(var)

var = "var fuera de la función"
mi_funcion2()
print(var)

# En este caso particular, la var dentro de la función es diferente en memoria a la que está fuera, por el scope de las funciones


# ============ Argumentos keyword =============



