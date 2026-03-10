# NOMBRE: Rayner Alexander Mora
# MATRICULA: 24-EISN-2-004

import pygame
import math
import constantes
import random

class arma():
    def __init__(self, image, imagen_bala):
        self.imagen_bala = imagen_bala
        self.image_original = image
        self.angulo = 0 
        self.imagen = self.image_original
        self.forma = self.imagen.get_rect()
        self.ultimo_disparo = pygame.time.get_ticks()
        

    def update(self, personaje):
        disparo_cooldown = constantes.COOLDOWN_BALAS

        bala = None

        # posicionar el arma respecto al personaje
        self.forma.center = personaje.forma.center 

        if personaje.flip == False: 
            self.forma.left = personaje.forma.right - 75
            self.rotar_arma(False)
        else:
            self.forma.right = personaje.forma.left + 75
            self.rotar_arma(True)

        #Poder mover la psitola usando el Mouse
        mouse_pos = pygame.mouse.get_pos()
        distancia_x = mouse_pos[0] - self.forma.centerx
        distancia_y = -(mouse_pos[1] - self.forma.centery)
        self.angulo = math.degrees(math.atan2(distancia_y, distancia_x))

        tiempo_actual = pygame.time.get_ticks()

        if pygame.mouse.get_pressed()[0] and (tiempo_actual - self.ultimo_disparo >= disparo_cooldown):
            bala = bullet(self.imagen_bala, self.forma.centerx, self.forma.centery, self.angulo)
            return bala


       
    
    def rotar_arma(self, rotar):
        if rotar == True:
            imagen_flip = pygame.transform.flip(self.image_original, flip_x=True, flip_y=False)

            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)

        else:
            imagen_flip = pygame.transform.flip(self.image_original, flip_x=False, flip_y=False)

            self.imagen = pygame.transform.rotate(imagen_flip, self.angulo)


    def dibujar(self, interfaz):
        interfaz.blit(self.imagen, self.forma)



class bullet (pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_original = image
        self.angulo = angle
        self.image = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        #Velocidad 
        self.delta_x = math.cos(math.radians(self.angulo))*constantes.VELOCIDAD_BALA
        
        self.delta_y = math.sin(math.radians(self.angulo))*constantes.VELOCIDAD_BALA
    
    def update(self, grupo_enemigos):
        daño = 0
        pos_daño = None
        
        self.rect.x += self.delta_x
        self.rect.y = self.rect.y + self.delta_y

        # ver si las balas salen de la pantalla
        if self.rect.right < 0 or self.rect.left > constantes.ANCHO_VENTANA or self.rect.bottom < 0 or self.rect.top > constantes.ALTO_VENTANA:
            self.kill()


        #Colision con enemigos
        for enemigo in grupo_enemigos:
            if enemigo.forma.colliderect(self.rect):
                daño = 15 + random.randint(-7, b= 7)
                pos_daño = enemigo.forma
                enemigo.energia = enemigo.energia - daño
                self.kill()
                break
        return daño, pos_daño

    def dibujar(self, interfaz):
        interfaz.blit(self.image, self.rect)
   

        #interfaz.blit (self.image, self.forma.centerx, self.forma.centery)