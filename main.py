import pygame
import constantes
from personaje import personaje

jugador = personaje(x=50, y=50)

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))

pygame.display.set_caption("SHOOT")

run = True
while run == True:

    jugador.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    
    pygame.display.update()

pygame.quit()           