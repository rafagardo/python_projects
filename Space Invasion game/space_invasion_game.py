import pygame
import random
import math
from pygame import mixer
import io
import os

# Solucionar el problema de la música en Windows
os.environ["SDL_AUDIODRIVER"] = "directsound"


# Inicializar Pygame
pygame.init()
mixer.init()


# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))


# Título e ícono
pygame.display.set_caption("Space Invasion")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("Fondo.jpg")


# Música de fondo
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.2)
mixer.music.play(-1)


# Jugador
img_jugador = pygame.image.load("nave-espacial.png")
jugador_x = 368
jugador_y = 500
jugador_x_change = 0


# Enemigos
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_change = []
enemigo_y_change = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_change.append(0.1)
    enemigo_y_change.append(50)


# Bala
balas = []
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_change = 0
bala_y_change = 0.5
bala_visible = False


# Función para convertir las fuentes de tipo String a tipo Bytes
def convertir_bytes(string):
    with open(string, "rb") as f:
        ttf_bytes = f.read()
    return io.BytesIO(ttf_bytes)


# Puntaje
puntaje = 0
fuente_como_bytes = convertir_bytes("Fastest.ttf")
fuente = pygame.font.Font(fuente_como_bytes, 32)
texto_x = 10
texto_y = 10


# Texto final del juego
fuente_game_over = pygame.font.Font(fuente_como_bytes, 64)


# Función para mostrar el texto final del juego
def mostrar_texto_final():
    game_over_texto = fuente_game_over.render("GAME OVER", True, (255, 255, 255))
    pantalla.blit(game_over_texto, (120, 200))


# Función para mostrar al jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Función para mostrar al enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


# Función para mostrar la bala
def bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# Función para detectar colisiones
def colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt((math.pow(x_1 - x_2, 2)) + (math.pow(y_1 - y_2, 2)))
    if distancia < 27:
        return True
    else:
        return False


# Función para mostrar el puntaje
def mostrar_puntaje(x, y):
    puntaje_texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(puntaje_texto, (x, y))


# Loop del juego
se_ejecuta = True
while se_ejecuta:

    # Fondo de la pantalla
    # pantalla.fill((205, 144, 228))
    pantalla.blit(fondo, (0, 0))

    # Eventos
    for evento in pygame.event.get():

        # Salir del juego
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Eventos del teclado
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_change = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_change = 0.3
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.play()
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -0.1
                    }
                balas.append(nueva_bala)

        # Detener el movimiento del jugador
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_change = 0

    # Actualizar la posición del jugador
    jugador_x += jugador_x_change

    # Límites de la pantalla del jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Actualizar la posición del enemigo
    for e in range(cantidad_enemigos):

        # Game Over
        if enemigo_y[e] > 500:
            for j in range(cantidad_enemigos):
                enemigo_y[j] = 2000
            mostrar_texto_final()
            break

        enemigo_x[e] += enemigo_x_change[e]

        # Límites de la pantalla del enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_change[e] = 0.3
            enemigo_y[e] += enemigo_y_change[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_change[e] = -0.3
            enemigo_y[e] += enemigo_y_change[e]

        # Colisión
        for bala in balas:
            colision_bala_enemigo = colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("Golpe.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(20, 200)
                break

        # Mostrar al enemigo
        enemigo(enemigo_x[e], enemigo_y[e], e)

        # Movimiento de la bala
        for bala in balas:
            bala["y"] += bala["velocidad"]
            pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
            if bala["y"] < 0:
                balas.remove(bala)
        for bala in balas:
            bala["y"] += bala["velocidad"]
            pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
            if bala["y"] < 0:
                balas.remove(bala)

    # Actualizar la posición de la bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        bala(bala_x, bala_y)
        bala_y -= bala_y_change


    # Mostrar al jugador
    jugador(jugador_x, jugador_y)


    # Mostrar el puntaje
    mostrar_puntaje(texto_x, texto_y)


    # Actualizar la pantalla
    pygame.display.update()



