alumnos = []

def agregar_alumnos(nombre, edad, calificaciones):
    lista_calificaciones = calificaciones.split()
    lista_calificaciones = [float(c) for c in lista_calificaciones]
    
    alumnos_info = None
    alumnos_info = {
        "nombre": nombre,
        "edad": edad,
        "calificaciones": lista_calificaciones
    }
    
    if alumnos_info is not None:
        alumnos.append(alumnos_info)
    else:
        print("Algo salio mal pa")

def mostrar_alumnos(agregar_alumnos):
    print(f"Nombre: {nombre_alumno}, Edad: {edad_alumno}, Calificaciones: {calificaciones_alumno}")

def promedio_alumno(alumnos):
    alumno_request = input("Nombre del alumno: ")
    for alumno in alumnos:
        if alumno["nombre"] == alumno_request:
            califs = alumno["calificaciones"]
            promedio = sum(califs) / len(califs)
            print(f"El promedio de {alumno_request} es: {promedio}")

# --- Flujo de prueba ---

nombre_alumno = input("Ingresa nombre: ")
edad_alumno = input("Ingresa edad alumno: ")
calificaciones_alumno = input("Ingresa calificaciones: ")

agregar_alumnos(nombre_alumno, edad_alumno, calificaciones_alumno)

mostrar_alumnos(agregar_alumnos)

promedio_alumno(alumnos)