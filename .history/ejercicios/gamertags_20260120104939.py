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

tag_invertido = crear_tag_invertido("Luisor")
print(f"El tag invertido es: {tag_invertido}")

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
    return primer_letra_nombre, primer_letra_apellido, restante_nombre, restante_apellido

tag_intercalado = crear_tag_intercalado("Luisasd", "Gadrds")
print(sep="tag_intercalado")