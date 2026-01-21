# Una función es un bloque de código en python que permite reutilizar esos mismos bloques

def mi_funcion(arg1, arg2):
    print(arg1)
    print(arg2)

mi_funcion("hola", "dos") # Los argumentos se corresponden con los parámetros



def saludo():
    return print("hola")

print(saludo())

def suma(a, b):
    sumar = a + b
    return sumar

print(suma(1, 2))

def datos(nombre, edad):
    saludo = nombre + edad
    return saludo

nombre = input("Cuál es tu nombre: ")
edad = input("cuál es tu edad: ")
print(input(f"Hola {nombre}, tienes {edad}"))