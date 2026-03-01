import pygame
import constantes

class personaje():
    def __init__(self, x, y):
        self.forma = pygame.Rect(0, 0, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE)
        
        self.forma.center = (x,y)

    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, rect = self.forma)
