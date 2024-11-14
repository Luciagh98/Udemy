import pygame
import random
import math
from pygame import mixer

#Iniciar pygame
pygame.init()


#Establecer el tamaño de la pantalla
pantalla = pygame.display.set_mode((800,600))

#Personalizar la pantalla.
#Editar el titulo de la pantalla:
pygame.display.set_caption("Invasión Espacial")
#Editar el icono de la pantalla:
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
#Podemos poner un fondo de pantalla personalizado, como una imagen
fondo = pygame.image.load("Fondo.jpg")
#Puntuación
puntaje = 0
fuente = pygame.font.Font("Fastest.ttf",32)
texto_x = 10 #Coordenadas
texto_y = 10 #Coordenadas

#Música de fondo
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.3) #Establecer el volumen
mixer.music.play(-1) #Para que se repita cada vez que termie

#Crear el jugador
#Para ubicar al "protagonista" hay que saber el tamaño de la pantalla para ubicar las otras partes.
img_jugador = pygame.image.load("cohete.png")
jugador_x = 368 #Posición sobre el eje x (800/2) - (64/2)
jugador_y = 500 #Posición sobre el eje y
jugador_x_cambio = 0

#Crear un conjunto de enemigos
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

#Crear al enemigo
for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0,736)) #800-64
    enemigo_y.append(random.randint(50,200)) #Altura aproximada
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)

#Crear la bala
balas = []
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500 #la misma altura que la nave
bala_x_cambio = 0
bala_y_cambio = 3 #será la velocidad de movimiento
bala_visible = False #para mostrarla o no

def jugador(x,y):
    pantalla.blit(img_jugador,(x,y)) #Similar a iniciar. Con x y y nos permite mover por la pantalla.

def enemigo(x,y,ene):
    pantalla.blit(img_enemigo[ene],(x,y)) #Similar a iniciar.

def disparar_bala(x, y):
    global bala_visible
    bala_visible = True #hacerla visible
    pantalla.blit(img_bala,(x + 16,y + 10)) #Para que no aparezca exactamente encima de la nave, sino arriba.

#Saber si hay o no una colisión entre los objetos
def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_1-x_2,2) + math.pow(y_2-y_1,2)) #raiz quadrada de la suma de (x2 - x1)^2 y (y2 - y1)^2
    if distancia < 27:
        return True
    else:
        return False

#Mostrar el puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255,255,255)) #Renderizar en pantalla
    pantalla.blit(texto,(x,y))

#Final del juego - texto
fuente_final = pygame.font.Font("Fastest.ttf",40)

def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO",True, (255,255,255))
    pantalla.blit(mi_fuente_final,(120,200)) #En el centro de la pantalla


#Hacer que el código se ejecute y se mantenga activa la pantalla. NO CON UN LOOP INFINITO

se_ejecuta = True
while se_ejecuta:
    # Cambiar el fondo de pantalla.
    pantalla.blit(fondo,(0,0))
    #Iterar dentro de los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: #Hacemos que en el momento que se cliquee la cruz roja de la pantalla (QUIT), se cierre el bucle.
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN: #Una tecla presionada, NO SOLTADA
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = +1
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.play()
                if not bala_visible: #Hacemos que si no esta visible, se ejecute el movimiento
                    bala_x = jugador_x
                    disparar_bala(bala_x,bala_y) #Para que aparezca la bala

        if evento.type == pygame.KEYUP: #Una tecla ya presionada, que se suelte
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #Establecemos que el valor de la x sea el del cambio segun la tecla presionada.
    jugador_x += jugador_x_cambio

    #Establecer los limites de la pantalla para que no se salga el jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736: #(800-64)
        jugador_x = 736

    #Modificar la ubicación del enemigo
    for e in range(cantidad_enemigos):
        #Si el enemigo llega al final, se acaba el juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break
        enemigo_x[e] += enemigo_x_cambio[e]

    #Establecer los limites de la pantalla para que se mueva dentro de ella
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736: #(800-64)
            enemigo_x_cambio[e] = -1
            enemigo_y[e] += enemigo_y_cambio[e]

         # Establecer una colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)

        # Hacemos que si hay colision, la bala vuelva a la posición inicial, se vuelva invisible, y sumemos puntaje.
        # Al dar al enemigo, hacemos que aparezca en otro punto aleatorio.
        if colision:
            sonido_colision = mixer.Sound("Golpe.mp3")
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)

        # Llamamos al enemigo en la pantalla
        enemigo(enemigo_x[e], enemigo_y[e],e)

    #Movimiento de la bala
    #Queremos disparar mas de una, por tanto, en el momento que llegue al limite la volvemos insisible
    #iniciando de nuevo el ciclo
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    #Para que no siga el trayecto de la nave
    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y -= bala_y_cambio

    #Llamamos al jugador en la pantalla
    jugador(jugador_x,jugador_y)

    #Mostrar puntos
    mostrar_puntaje(texto_x,texto_y)

    #Actualizar
    pygame.display.update()






