alumnos = []
nombre_alumno = input("Ingresa nombre: ")
edad_alumno = input("Ingresa edad alumno: ")
calificaciones_alumno = input("Ingresa calificaciones: ")

def agregar_alumnos(nombre, edad, calificaciones):
    alumnos_info = None
    alumnos_info = {"nombre": {nombre_alumno},
                    "edad": {edad_alumno},
                    "calificaciones": [{calificaciones_alumno}]}
    # print(alumnos_info)
    if alumnos_info is not None:
        alumnos.append(alumnos_info)
    else:
        print("Algo salio mal pa")

agregar_alumnos(nombre_alumno, edad_alumno, calificaciones_alumno)

def mostrar_alumnos(agregar_alumnos):
    print(f"Nombre: {nombre_alumno}, Edad: {edad_alumno}, Calificaciones: {calificaciones_alumno}")

mostrar_alumnos(agregar_alumnos)
print(len(alumnos))

def promedio_alumno(alumnos):
    alumno_request = input("Nombre del alumno: ")
    alumnos_iterable = iter(alumnos)
    



