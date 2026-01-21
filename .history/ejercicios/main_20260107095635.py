# alumnos = []
# print(alumnos)
# alumnos.append(1)
# print(alumnos)


alumnos = {}
print(alumnos)
nombre_alumno = input("Ingresa nombre: ")
edad_alumno = input("Ingresa edad alumno: ")
calificaciones = input("Ingresa calificaciones: ")

def agregar_alumnos(nombre, edad, calificaciones):
    alumnos.update({"nombre": {nombre_alumno}})

agregar_alumnos(nombre_alumno)
print(alumnos)