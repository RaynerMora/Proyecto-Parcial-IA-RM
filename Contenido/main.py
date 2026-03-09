#Aqui importe constantes y personaje para mejor facilidad y manejo del codigo.

import pygame
import constantes as constantes
from personaje import personaje
from arma import arma
from text_daño import Damagetext
from items import Item
from mundo import Mundo
import os
import csv

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
#Energia
vida_vacia = pygame.image.load("assets/imagenes/items/dead.png").convert_alpha()
vida_vacia = escalar_img(vida_vacia, constantes.SCALA_VIDA)

vida_half = pygame.image.load("assets/imagenes/items/half_live.png").convert_alpha()
vida_half = escalar_img(vida_half, constantes.SCALA_VIDA)

vida_llena = pygame.image.load("assets/imagenes/items/full_live.png").convert_alpha()
vida_llena = escalar_img(vida_llena, constantes.SCALA_VIDA)

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

#IMG del MUNDO
tile_list = []
for x in range(constantes.TILE_TYPES):
    tile_image = pygame.image.load(f"assets/imagenes/tiles/tile ({x+1}).png")
    tile_image = pygame.transform.scale(tile_image, size=(constantes.TITLE_SIZE, constantes.TITLE_SIZE))
    tile_list.append(tile_image)

#CARGAR IMAGENES DE LOS ITEMS
pocion_roja = pygame.image.load("assets/imagenes/items/pocion_vida.png")
pocion_roja = escalar_img(pocion_roja, scale=0.5)

monedas_images = []
ruta_img = "assets/imagenes/items/moneda"
num_moneda_img = contar_elementos(ruta_img)
for i in range(num_moneda_img):
    img = pygame.image.load(f"assets/imagenes/items/moneda/moneda_{i+1}.png")
    img = escalar_img(img, scale=1)
    monedas_images.append(img)

def dibujar_score(texto, fuente, color, x, y):
    img = fuente.render(texto, True, color)
    ventana.blit(img, (x,y))

#Vida jugador
def vida_jugador():
    v_mitad_dibujado = False
    for i in range(5):
        if jugador.energia >= ((i+1)*20):
            ventana.blit(vida_llena, dest=(5+i*50, 5))
        elif jugador.energia % 20 > 0 and v_mitad_dibujado == False:
            ventana.blit(vida_half, dest=(5+i*50, 5))
            v_mitad_dibujado = True
        else:
            ventana.blit(vida_vacia, dest=(5 + i * 50, 5))

world_data = []

for fila in range(constantes.FILAS):
    filas = [7] * constantes.COLUMNAS
    world_data.append(filas)

#Cargar archivo con el nivel
with open("niveles/nivel_test.csv", newline="") as csvfile:
          reader = csv.reader(csvfile, delimiter=",")
          for x, fila in enumerate(reader):
              for y, columna in enumerate(fila):
                  world_data[x][y] = int(columna)
print(fila)




word = Mundo()
word.process_data(world_data, tile_list)



def dibujar_grid():
    for x in range(30):
        pygame.draw.line(ventana, constantes.BLANCO, start_pos=(x*constantes.TITLE_SIZE, 0), end_pos=(x*constantes.TITLE_SIZE, constantes.ALTO_VENTANA)) 

        pygame.draw.line(ventana, constantes.BLANCO, start_pos=(0, x * constantes.TITLE_SIZE), end_pos=(constantes.ANCHO_VENTANA, x * constantes.TITLE_SIZE)) 



#Cargando imagen del jugador y ajustando tamaño

jugador = personaje(50, 50, animaciones, energia = 20)

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
grupo_items = pygame.sprite.Group()

moneda = Item(350, 25, 0, monedas_images)
pocion_roja = Item(380, 55, 1, [pocion_roja])

grupo_items.add(moneda)
grupo_items.add(pocion_roja)

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

    dibujar_grid()

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

    #ACTUALIZAR items
    grupo_items.update(jugador)

    #dibujar mundo
    word.draw(ventana)

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


    #Dibujar vida
    vida_jugador()
    
    #dibujar texto_daño
    grupo_damage_text.draw(ventana)
    dibujar_score(f"Score: {jugador.score}", fuentes, color=(255,255,0), x=700, y=5)

    #Dibujar los items en pantalla
    grupo_items.draw(ventana)




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