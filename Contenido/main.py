#Aqui importe constantes y personaje para mejor facilidad y manejo del codigo.

import pygame
import constantes as constantes
from personaje import personaje
from arma import arma
from text_daño import Damagetext
import os

#Funciones:
#Escalando las imagenes para mostrar movimientos del jugador

def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_imagen

#F, contar elementos 
def contar_elementos(directorio):
    return len(os.listdir(directorio))


#listar nombres de los elementos 
def nombre_carpetas(directorio):
    return os.listdir(directorio)



#Inicializacion del personaje, ventana del juego y nombre.

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))

pygame.display.set_caption("SHOOT")

#Fuentes
fuentes = pygame.font.Font("assets/fonts/ThaleahFat.ttf", size=25)


#Importar imagenes
#Personaje
animaciones = []
for i in range (1, 8):
    img = pygame.image.load(f"assets/imagenes/characters/player/player_{i}.png")

    img = escalar_img(img, constantes.SCALA_PERSONAJE) 
    animaciones.append(img)

#Enemigos
directorio_enemigos = "assets/imagenes/characters/enemigos"
tipo_enemigos = nombre_carpetas(directorio_enemigos)
animaciones_enemigos = []
for eni in tipo_enemigos:
    lista_temp = []
    ruta_temp = f"assets/imagenes/characters/enemigos/{eni}"
    num_animaciones = contar_elementos(ruta_temp)

    for i in range(num_animaciones):
        img_enemigo = pygame.image.load(f"{ruta_temp}//{eni}_{i+1}.png").convert_alpha()
        img_enemigo = escalar_img(img_enemigo, constantes.SCALA_ENEMIGO)
        lista_temp.append(img_enemigo)
    animaciones_enemigos.append(lista_temp)


#Arma
imagen_pistola = pygame.image.load(f"assets/imagenes/Armas/Arma.png")
imagen_pistola = escalar_img(imagen_pistola, constantes.SCALA_ARMA)

#Balas
imagen_balas = pygame.image.load(f"assets/imagenes/Armas/bala.png").convert_alpha()
print(imagen_balas)
imagen_balas = pygame.transform.scale(imagen_balas, constantes.SCALA_BALA)


#Cargando imagen del jugador y ajustando tamaño

jugador = personaje(50, 50, animaciones, energia = 100)

#Enemigo clase personaje

guardian = personaje(400, 300, animaciones_enemigos[0], energia=100)

guardian_esqueleto = personaje(200, 200, animaciones_enemigos[1],energia=100)

#Lista de Enemigos
lista_enemigos = []
lista_enemigos.append(guardian)
lista_enemigos.append(guardian_esqueleto)
print(lista_enemigos)

#Arma de la clase arma 

pistola = arma(imagen_pistola, imagen_balas)

#Grupo de sprites
grupo_damage_text = pygame.sprite.Group()
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

    #Act, estado enemigos
    for ene in lista_enemigos:
        ene.update()
        print(ene.energia)

    #Act, estado Arma
    bala = pistola.update(jugador)
    if bala:
        grupo_balas.add(bala)
    for bala in grupo_balas:
        damage, pos_damage= bala.update(lista_enemigos)
        if damage:
           damage_text = Damagetext(pos_damage.centerx,pos_damage.centery, str(damage), fuentes, constantes.ROJO)
           grupo_damage_text.add(damage_text)

    #Act daño

    grupo_damage_text.update()

    #Dibujar al jugador
    jugador.dibujar(ventana)

    #Dibujar al enemigo
    for ene in lista_enemigos:
        ene.dibujar(ventana)

    #Dibujar arma
    pistola.dibujar(ventana)

    #Dibujar balas
    for bala in grupo_balas:
        bala.dibujar(ventana)
    
    #dibujar texto_daño
    grupo_damage_text.draw(ventana)

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