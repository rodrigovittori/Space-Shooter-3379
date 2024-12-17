#pgzero
import random

""" > [M6.L1] · Actividad #5: "Colisiones"

Kenney assets:

Kodland: https://kenney.nl/assets/space-shooter-extension
Extra: https://kenney.nl/assets/space-shooter-redux
Planetas: https://kenney.nl/assets/planets
UI: https://kenney.nl/assets/ui-pack-sci-fi


Objetivo: Implementar colisiones
Prox. Actividad: Implementar GAME OVER

Paso Nº 1: Agregamos una fn llamada comprobar_colisiones()
Paso Nº 2: Agregamos una llamada a comprobar_colisiones() en nuestro update()
Paso Nº 3: Modificamos spawn_nvo_enemigo() para que las naves enemigas NO se superpongan

    ##################
   # VENTANA PGZERO #
  ################## """

WIDTH = 600
HEIGHT = 450

TITLE = "GUERRA GALÁCTICA"
FPS = 30

# Objetos y Variables
CANT_ENEMIGOS = 5 # Cantidad de enemigos a spawnear

nave = Actor("ship", (300,300))
fondo = Actor("space")

# Listas
lista_enemigos = []

################################

"""  #####################
    # FUNCIONES PROPIAS #
   #####################  """

def spawn_nvo_enemigo(tipo=""):
    # Determinar tipo de enemigo a añadir:
    if tipo == "":
        tipo = "enemy"

    pos_valida = False

    while (not pos_valida):
    
        # Setear coordenadas random (importamos la librería)
        x = random.randint(50, WIDTH-50)
        y = random.randint(-200, -50)

        # Creamos un nvo_enemigo según su tipo:
        nvo_enemigo = Actor(tipo, (x, y))
    
        # Verificamos que nuestro nvo_enemigo NO se superponga con otro
        # Nota: más adelante veremos collidelist que sería una mejor solución a este caso
        pos_valida = True # Defino como "válida" la posición, hasta que encuentre lo contrario
      
        for nave_enemiga in lista_enemigos:
            # recorro la lista de enemigos y chequeo las colisiones
            if  nvo_enemigo.colliderect(nave_enemiga):
                pos_valida = False

        # Si el for termina y la posición NO es válida, vá a repetirse el while

    # Cuando ya validé la posición de mi nvo_enemigo, configuro lo demás
    
    """ Nota: Si yo quiero que la velocidad de los enemigos sea un factor
              de la dificultad del juego, en lugar de ser random p/cada
              nave, puedo crear una variable global llamada "velocidad_naves_enemigas"
              (o algo así) y actualizarlo cuando lo necesite 

              > Si mis enemigos tienen cambios según su tipo:
                  if tipo == "enemy":
                  *modificamos lo que tengamos que modificar: velocidad, salud, bonus que dropea, etc*
    """

    nvo_enemigo.velocidad = random.randint(4, 8) # o variable global
    # Cuando mi nuevo enemigo está listo, lo agrego a la lista:
    lista_enemigos.append(nvo_enemigo)
    #####################################################################

def comprobar_colisiones():
    # Comprobar colisiones con enemigos
    for nave_enemiga in lista_enemigos:
        if nave.colliderect(nave_enemiga):
            # Hubo colisión :(
            exit() # cerramos el juego
            # To-do: modificar por game_over

def mov_flota_enemiga():
    for nave_enemiga in lista_enemigos:

        if (nave_enemiga.y > (HEIGHT + nave_enemiga.height)): # Si se salió de la pantalla
            # La reciclamos:
            nave_enemiga.y = random.randint(-200, -50)
            nave_enemiga.x = random.randint(50, WIDTH - 50)
            # Nota: si cambiamos la velocidad según la dificultad, modificar ésto:
            nave_enemiga.velocidad = random.randint(4, 8) # o variable global

        else:
            nave_enemiga.y += nave_enemiga.velocidad

# To-do: convertir a funcion Inicializar/Reiniciar Juego
for enemigo in range(CANT_ENEMIGOS):
    spawn_nvo_enemigo()


"""  #####################
    # FUNCIONES PG-ZERO #
   #####################  """

def draw():
    fondo.draw()

    for nave_enemiga in lista_enemigos:
        nave_enemiga.draw()
    
    texto_temp = "Coord: (x: " + str(int(nave.x)) + ", y: " + str(int(nave.y)) + ")"
    screen.draw.text(texto_temp, midleft=(20, 20), color = "white", fontsize = 24)
    
    #screen.draw.text(TITLE, center=(300, 100), color="white", background="black")
    nave.draw()
    
def on_mouse_move(pos):
  nave.pos = pos

def update(dt):
    mov_flota_enemiga()
    comprobar_colisiones()