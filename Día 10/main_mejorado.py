import pygame
import random
import math
from pygame import mixer

# Dimensiones de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# Colores
BLANCO = (255, 255, 255)

# Velocidades
VEL_JUGADOR = 1
VEL_BALA = 3

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

# Cargar imágenes
img_jugador = pygame.image.load("cohete.png")
img_enemigo = pygame.image.load("enemigo.png")
img_bala = pygame.image.load("bala.png")
fondo = pygame.image.load("Fondo.jpg")

# Fuente de texto
fuente = pygame.font.Font("Fastest.ttf", 32)

# Música de fondo
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Posición inicial del jugador
jugador_x = ANCHO_PANTALLA // 2 - img_jugador.get_width() // 2
jugador_y = 500

# Función para mostrar el jugador en la pantalla
def mostrar_jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Función para mostrar un enemigo en la pantalla
def mostrar_enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))

# Función para mostrar una bala en la pantalla
def mostrar_bala(x, y):
    pantalla.blit(img_bala, (x, y))

# Función para mostrar el puntaje en la pantalla
def mostrar_puntaje(puntaje):
    texto = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
    pantalla.blit(texto, (10, 10))

# Bucle principal del juego
se_ejecuta = True
while se_ejecuta:
    pantalla.blit(fondo, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x -= VEL_JUGADOR
            elif evento.key == pygame.K_RIGHT:
                jugador_x += VEL_JUGADOR
            elif evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x + img_jugador.get_width() // 2 - img_bala.get_width() // 2
                    bala_y = jugador_y
                    bala_visible = True
                    mixer.Sound("disparo.mp3").play()

    if jugador_x < 0:
        jugador_x = 0
    elif jugador_x > ANCHO_PANTALLA - img_jugador.get_width():
        jugador_x = ANCHO_PANTALLA - img_jugador.get_width()

    if bala_visible:
        mostrar_bala(bala_x, bala_y)
        bala_y -= VEL_BALA
        if bala_y < 0:
            bala_visible = False

    mostrar_jugador(jugador_x, jugador_y)
    mostrar_puntaje(puntaje)

    pygame.display.update()
