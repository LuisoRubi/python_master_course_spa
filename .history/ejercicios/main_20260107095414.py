# alumnos = []
# print(alumnos)
# alumnos.append(1)
# print(alumnos)


alumnos = {}


def agregar_alumnos(nombre):
    nombre_alumno = input("Ingresa nombre: ")
    alumnos.update({"nombre": "{nombre_alumno}"})

agregar_alumnos(nombre_alumno)
print(alumnos)