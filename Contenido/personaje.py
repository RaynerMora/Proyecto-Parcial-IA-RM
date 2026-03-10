# NOMBRE: Rayner Alexander Mora
# MATRICULA: 24-EISN-2-004

import pygame
import constantes as constantes 
import math

class personaje():

    def __init__(self, x, y, animaciones, energia, tipo):
        self.score = 0
        self.energia = energia
        self.vivo = True
        self.flip = False
        self.animaciones = animaciones

        #imagen de animacion
        self.frame_index = 1
        #para almacenar hora en milisegundos desde se inicio pygame.
        self.update_time = pygame.time.get_ticks()
        self.image = animaciones[self.frame_index]
        self.forma = self.image.get_rect()
        self.forma.center = (x,y)
        self.tipo = tipo
        self.golpe = False
        self.ultimo_golpe = pygame.time.get_ticks()
        self.golpe = False
        self.ultimo_golpe = pygame.time.get_ticks()


    def movimiento(self, delta_x, delta_y, obstaculos_tiles):
        posicion_pantalla = [0, 0]
        if delta_x < 0:
            self.flip = True
        elif delta_x > 0:
            self.flip = False

        self.forma.x = self.forma.x + delta_x
        for obstacle in obstaculos_tiles:
            if obstacle[1].colliderect(self.forma):
                if delta_x > 0:
                    self.forma.right = obstacle[1].left
                if delta_x < 0:
                    self.forma.left = obstacle[1].right

        self.forma.y = self.forma.y + delta_y
        for obstaculo in obstaculos_tiles:
            if obstaculo[1].colliderect(self.forma):
                if delta_y > 0:
                    self.forma.bottom = obstaculo[1].top
                if delta_y < 0:
                    self.forma.top = obstaculo[1].bottom

        #Logica solo jugador no enemigos
        #actulizar pantalla segun posicion
         #mover la camara izquierda o derecha

        if self.forma.right > (constantes.ANCHO_VENTANA - constantes.LIMITE_PANTALLA):
            posicion_pantalla[0] = (constantes.ANCHO_VENTANA - constantes.LIMITE_PANTALLA) - self.forma.right
            self.forma.right = constantes.ANCHO_VENTANA - constantes.LIMITE_PANTALLA

        if self.forma.left < constantes.LIMITE_PANTALLA:
                posicion_pantalla[0] = constantes.LIMITE_PANTALLA - self.forma.left

                self.forma.left = constantes.LIMITE_PANTALLA
            
        #mover la camara arriba o abajo

        if self.forma.bottom > (constantes.ALTO_VENTANA - constantes.LIMITE_PANTALLA):
                posicion_pantalla[1] = (constantes.ALTO_VENTANA - constantes.LIMITE_PANTALLA) - self.forma.bottom

                self.forma.bottom = constantes.ALTO_VENTANA - constantes.LIMITE_PANTALLA

        if self.forma.top < constantes.LIMITE_PANTALLA:
                posicion_pantalla[1] = constantes.LIMITE_PANTALLA - self.forma.top

                self.forma.top = constantes.LIMITE_PANTALLA

        return posicion_pantalla
        
    def enemigos(self, jugador, obstaculos_tiles, posicion_pantalla):
        ene_dx = 0
        ene_dy = 0

        #reposicion enemigos segun camara o pantalla
        self.forma.x += posicion_pantalla[0]
        self.forma.y += posicion_pantalla[1]

        #distancia con jugador
        distancia = math.sqrt(((self.forma.centerx - jugador.forma.centerx)**2)+((self.forma.centery - jugador.forma.centery)**2))

        if distancia < constantes.RANGO:
            if self.forma.centerx > jugador.forma.centerx:
             ene_dx = - constantes.VELOCIDAD_ENEMIGO

            if self.forma.centerx < jugador.forma.centerx:
             ene_dx = constantes.VELOCIDAD_ENEMIGO

            if self.forma.centery > jugador.forma.centery:
             ene_dy = -constantes.VELOCIDAD_ENEMIGO

            if self.forma.centery < jugador.forma.centery:
             ene_dy = constantes.VELOCIDAD_ENEMIGO

        self.movimiento(ene_dx, ene_dy, obstaculos_tiles)

        #atacar jugador
        if distancia < constantes.RANGO_ATAQUE and jugador.golpe == False:
            jugador.energia -= 10
            jugador.golpe = True
            jugador.ultimo_golpe = pygame.time.get_ticks()




    def update(self):
        #Comprobar si personaje a muerto
        if self.energia <= 0:
            self.energia = 0
            self.vivo = False

        #volver recibir daño 
        golpe_cooldown = 1000
        if self.tipo == 1:
            if self.golpe == True:
                if pygame.time.get_ticks() - self.ultimo_golpe > golpe_cooldown:
                    self.golpe = False

        coldowm_animacion = 500
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= coldowm_animacion:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones):
            self.frame_index = 0

    def dibujar(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(imagen_flip, self.forma)
        

       # pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, rect = self.forma, width = 1)
