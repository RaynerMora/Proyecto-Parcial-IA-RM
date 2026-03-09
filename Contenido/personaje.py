import pygame
import constantes as constantes  

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


    def movimiento(self, delta_x, delta_y ):
        posicion_pantalla = [0, 0]
        if delta_x < 0:
            self.flip = True
        elif delta_x > 0:
            self.flip = False

        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y

        #Logica solo jugador no enemigos
        if self.tipo == 1:
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
        
    def enemigos(self, posicion_pantalla):
        #reposicion enemigos segun camara o pantalla
        self.forma.x += posicion_pantalla[0]
        self.forma.y += posicion_pantalla[1]




    def update(self):
        #Comprobar si personaje a muerto
        if self.energia <= 0:
            self.energia = 0
            self.vivo = False

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
