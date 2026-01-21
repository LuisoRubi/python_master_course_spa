def mostrar_titulo():
    """Muestra la cabecera de la función
    """
    titulo = r"""
 $$$$$$\                                           $$$$$$$$\                            
$$  __$$\                                          \__$$  __|                           
$$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$\  $$ | $$$$$$\   $$$$$$\   $$$$$$$\ 
$$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\ $$ | \____$$\ $$  __$$\ $$  _____|
$$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |$$ |  \__|$$ | $$$$$$$ |$$ /  $$ |\$$$$$$\  
$$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|$$ |      $$ |$$  __$$ |$$ |  $$ | \____$$\ 
\$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\ $$ |      $$ |\$$$$$$$ |\$$$$$$$ |$$$$$$$  |
 \______/  \_______|\__| \__| \__| \_______|\__|      \__| \_______| \____$$ |\_______/ 
                                                                    $$\   $$ |          
                                                                    \$$$$$$  |          
                                                                     \______/
                        By: Luiso Rubí Dev                                                        
"""
    print(titulo)

def crear_tag_basico(nombre):
    """Crea un tag basico usando las primeras cuatro letras

    Args:
        nombre (str): Nombre del usuario
    Return:
        str: Gamertag basico
    """
    tag = nombre[:4]
    return tag

tag_basico = crear_tag_basico("Luisod")
print(f"El tag básico es: {tag_basico}")

def crear_tag_invertido(nombre):
    """Crea tag invirtiendo el nombre del usuario

    Args:
        nombre (str): Nombre de usuario
    Return:
        str: Nombre invertido
    """
    tag = nombre[::-1] #recorre el texto de uno en uno hacia atrás
    return tag

# tag_invertido = crear_tag_invertido("Luisor")
# print(f"El tag invertido es: {tag_invertido}")

def crear_tag_intercalado(nombre, apellido):
    """Creates a intercalated tag with full name

    Args:
        nombre (str): User's name
        apellido (str): User's last name
    Return:
        str: intercalted gamertag with user's full name
    """
    primer_letra_nombre = nombre[0]
    primer_letra_apellido = apellido[0]
    restante_nombre = nombre[1:]
    restante_apellido = apellido[1:]
    print(primer_letra_nombre, primer_letra_apellido, restante_nombre, restante_apellido, sep="")

# tag_intercalado = crear_tag_intercalado("Luiso", "Rubi")

def crear_tag_elite(nombre):
    """Create tag just with first two letters and last two letters of user's name

    Args:
        nombre (str): user's name
    Returns:
        str: gamertag with 4 characters
    """
    first_letters = nombre[:2]
    last_letters = nombre[-2:]
    print(first_letters, last_letters, sep="")

# tag_elite = crear_tag_elite("Robertito")

def crear_tag_con_numero(nombre, numero_favorito):
    """Creates gamertag with user's name and favorite number

    Args:
        nombre (str): user's name
        numero_favorito (int): user's fav number
    Return:
        str: gamertag with letters and numbers
    """
    user_name = nombre[:5]
    fav_num = numero_favorito
    print(user_name, fav_num, sep="")


# tag_con_numero = crear_tag_con_numero("Kkjncxsdsd", 45)

def mostrar_estadisticas(nombre):
    """Shows name statistics

    Args:
        nombre (str): Shows info about user's name that will be used to generate gamertag
    Returns:
        str: List with user's info
    """
    
    print("ℹ️  ESTADÍSTICAS DE TU NOMBRE:")
    print(f"Nombre completo: {nombre}")
    print(f"Longitud del nombre: {len(nombre)}")
    print(f"Primera Letra: {nombre[0]}")
    print(f"Última letra: {nombre[-1]}")

# mostrar_estadisticas("Luis")

# Flujo de prueba 
mostrar_titulo()

print("\n")

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
numero_favorito = input("Ingresa tu número favorito: ")

mostrar_estadisticas(nombre)

print("\n")
print("==================================")
print("🏜️  TUS OPCIONES DE GAMERTAG SON: ")
print("==================================")
print("\n")

print(f"1. TAG BÁSICO: {crear_tag_basico(nombre)}")
print(f"2. TAG INVERTIDO: {crear_tag_invertido(nombre)}")
print(f"3. TAG INTERCALADO: {crear_tag_intercalado(nombre, apellido)}")
print(f"4. TAG ELITE: {crear_tag_elite(nombre)}")
print(f"5. TAG CON NÚMERO: {crear_tag_con_numero(nombre, numero_favorito)}")

print("\n")
print("==================================")
print("👻 ELIGE EL QUÉ MAS TE GUSTE Y DISFRUTA TU JUEGO")