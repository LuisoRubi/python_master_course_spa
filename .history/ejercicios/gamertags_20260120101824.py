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