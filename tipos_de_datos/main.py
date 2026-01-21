# class Guerrero():
#     """Define una clase de guerrero
#     """
#     def __init__(self, raza, arma, poder_especial, potencia):
#         """Inicializa los atributos de instancia de la clase Guerrero

#         Args:
#             raza (_string_): Define la raza de nuestro guerrero
#             arma (string): Define el arma que usa el guerrero
#             poder_especial (string): Define el poder especial del guerrero
#         """
#         self.raza = raza
#         self.arma = arma
#         self.poder_especial = poder_especial
#         self.potencia = potencia
    
#     def especificaciones_guerrero(self):
#         """Muestra las especificaciones del guerrero
#         """
#         print("Has elegido al siguiente guerrero: ", 
#             "\nRaza: ", self.raza,
#             "\nArma: ", self.arma, 
#             "\nPoder Especial: ", self.poder_especial,
#             "\nPotencia: {} cv".format(self.potencia))
    

# guerrero1 = Guerrero("Hombre lobo", "Guadaña de mano", "Tormenta licantrópica", 450)
# print(guerrero1.especificaciones_guerrero())


# class Libro():
    
#     def __init__(self, titulo, autor, isbn):
          
#         self._titulo = titulo
#         self._autor = autor
#         self._isbn = isbn
#         self._disponible = True
    
#     def informacion(self):
        
#         print("La información del libro es: ", 
#                 "\nTitulo: ", self._titulo,
#                 "\nTitulo: ", self._autor,
#                 "\nISBN :", self._isbn,
#                 "\nDisponible: ", self._disponible)
        
#     def prestar_libro(self, prestado):
        
#         if prestado == self._disponible:
#             not prestado
#         else:
            

# libro1 = Libro("El llano", "Nunez", "KLHNAE6DS")
# print(libro1.informacion())