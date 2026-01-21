alumnos = []
print(alumnos)

nombre_alumno = input("Ingresa nombre: ")
edad_alumno = input("Ingresa edad alumno: ")
calificaciones_alumno = input("Ingresa calificaciones: ")

def agregar_alumnos(nombre, edad, calificaciones):
    alumnos_info = None
    alumnos_info = {"nombre": {nombre_alumno},
                    "edad": {edad_alumno},
                    "calificaciones": {calificaciones_alumno}}
    return alumnos_info
    # print(alumnos_info)
    # if alumnos_info is not None:
    #     print("El diccionario se creo correctamente")
    # else:
    #     print("Algo salio mal pa")

agregar_alumnos(nombre_alumno, edad_alumno, calificaciones_alumno)

alumnos.append(alumnos_info)
print(alumnos)
