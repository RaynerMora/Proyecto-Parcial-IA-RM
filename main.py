#Aqui importe constantes y personaje para mejor facilidad y manejo del codigo.

import pygame
import constantes
from personaje import personaje

#Inicializacion del personaje, ventana del juego y nombre.

jugador = personaje(x=50, y=50)

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))

pygame.display.set_caption("SHOOT")

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

   
    jugador.dibujar(ventana)

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