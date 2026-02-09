class Warrior:
    puntos = 300
    
    def nivel_de_daño(self): # Recordar usar self como primer parámetro casi obligatorio en cada método que creo y esto es porque con slef estoy indicando que existe una referencia a sí misma y esto evita errores con el namespace, scoop y todo ese rollo. 
        """Este método devuelve el puntaje de daño que el personaje puede causar
        """
        print("Daño causado: ", self.puntos)

guts = Warrior()
geralt = Warrior()

guts.nivel_de_daño()
print(guts.puntos)