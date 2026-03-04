import pygame
import math

class arma():
    def __init__(self, image):
        self.image_original = image
        self.angulo = 0 
        self.imagen = pygame.transform.rotate(self.image_original, self.angulo)
        self.forma = self.imagen.get_rect()

    def update(self, personaje):
        self.forma.center = personaje.forma.center 

        if personaje.flip == False: 
            self.forma.left = personaje.forma.right - 65
            self.rotar_arma(False)

        if personaje.flip == True: 
            self.forma.right = personaje.forma.left + 65
            self.rotar_arma(True)

    #Poder mover la psitola usando el Mouse
        mouse_pos = pygame.mouse.get_pos()
        distancia_x = mouse_pos[0] - self.forma.centerx
        distancia_y = -(mouse_pos[1] - self.forma.centery)
        self.angulo = math.degrees(math.atan2(distancia_y, distancia_x))

    
    def rotar_arma(self, rotar):
        if rotar == True:
            imagen_flip = pygame.transform.flip(self.image_original, flip_x=True, flip_y=False)

            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)

        else:
            imagen_flip = pygame.transform.flip(self.image_original, flip_x=False, flip_y=False)

            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)


    def dibujar(self, interfaz):
        self.imagen = pygame.transform.rotate(self.imagen, self.angulo)
        interfaz.blit(self.imagen, self.forma)
