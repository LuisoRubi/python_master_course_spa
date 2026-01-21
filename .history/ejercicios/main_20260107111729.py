alumnos = []

def agregar_alumnos(nombre, edad, calificaciones):
    alumnos_info = None
    alumnos_info = {"nombre": nombre, # no usar {} ya que si no se convierte en un set, poner variables sin {}
                    "edad": edad,
                    "calificaciones": [calificaciones]}
    # print(alumnos_info)
    if alumnos_info is not None:
        alumnos.append(alumnos_info)
    else:
        print("Algo salio mal pa")

agregar_alumnos(nombre, edad, calificaciones)

def mostrar_alumnos(agregar_alumnos):
    print(f"Nombre: {nombre_alumno}, Edad: {edad_alumno}, Calificaciones: {calificaciones_alumno}")

mostrar_alumnos(agregar_alumnos)
print(len(alumnos))

def promedio_alumno(alumnos):
    alumno_request = input("Nombre del alumno: ")
    # alumnos_iterable = iter(alumnos)
    for alumno_request in alumnos_iterable:
        print("hasta aqui va bien")

promedio_alumno(alumnos)
    
# --- Flujo de prueba ---

nombre = input("Ingresa nombre: ")
edad = input("Ingresa edad alumno: ")
calificaciones = input("Ingresa calificaciones: ")


