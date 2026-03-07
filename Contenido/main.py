#Aqui importe constantes y personaje para mejor facilidad y manejo del codigo.

import pygame
import constantes as constantes
from personaje import personaje
from arma import arma

#Inicializacion del personaje, ventana del juego y nombre.

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))

pygame.display.set_caption("SHOOT")

#Escalando las imagenes para mostrar movimientos del jugador

def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_imagen

#Importar imagenes
#Personaje
animaciones = []
for i in range (1, 8):
    img = pygame.image.load(f"Proyecto-Parcial-IA-RM/contenido/assets/imagenes/characters/player/player_{i}.png")

    img = escalar_img(img, constantes.SCALA_PERSONAJE) 
    animaciones.append(img)

#Arma
imagen_pistola = pygame.image.load(f"Proyecto-Parcial-IA-RM/contenido/assets/imagenes/Armas/Arma.png")
imagen_pistola = escalar_img(imagen_pistola, constantes.SCALA_ARMA)

#Balas
imagen_balas = pygame.image.load(f"Proyecto-Parcial-IA-RM/contenido/assets/imagenes/Armas/bala.png").convert_alpha()
print(imagen_balas)
imagen_balas = pygame.transform.scale(imagen_balas, constantes.SCALA_BALA)


#Cargando imagen del jugador y ajustando tamaño

jugador = personaje(50, 50, animaciones )

#Arma de la clase arma 

pistola = arma(imagen_pistola, imagen_balas)

#Grupo de sprites
grupo_balas = pygame.sprite.Group()


#Definir las variables del movimiento, jugador.
mover_derecha = False
mover_izquierda = False
mover_arriba = False
mover_abajo = False

#Controlar los fragmentos por segundo

reloj = pygame.time.Clock()

run = True
while run == True:

    #Especificar la velocidad
    reloj.tick(constantes.FPS)

    
    ventana.fill(constantes.COLOR_FONDO)

    #Calcular movimiento del jugador.

    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD
    print(f"{delta_x},{delta_y}")

    #Mover al jugador
    jugador.movimiento(delta_x, delta_y)

    #Act, estado del jugador
    jugador.update()

    #Act, estado Arma
    bala = pistola.update(jugador)
    if bala:
        grupo_balas.add(bala)
    for bala in grupo_balas:
        bala.update()

    #Dibujar al jugador
    jugador.dibujar(ventana)

    #Dibujar arma
    pistola.dibujar(ventana)

    #Dibujar balas
    for bala in grupo_balas:
        bala.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

        #TECLADO

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_s:
                mover_abajo = True

        #Para marcar cuando soltamos la tecla

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_s:
                mover_abajo = False

            
    pygame.display.update()

pygame.quit()           