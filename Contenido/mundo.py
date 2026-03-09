import constantes
from items import Item
from personaje import personaje

obstaculos = [0, 1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 66, 67, 36, 37]

class Mundo():
    def __init__(self):
        self.map_tiles = []
        self.obstaculos_tiles = []
        self.exit_tile = None
        self.lista_item = []
        self.lista_enemigo = []

    def process_data(self, data, tile_list, item_imagenes, animacion_enemigos):
        self.level_legth = len(data)
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                image = tile_list[tile]
                image_rect = image.get_rect()
                image_x = x * constantes.TITLE_SIZE
                image_y = y * constantes.TITLE_SIZE
                image_rect.center = (image_x, image_y)
                tile_data = [image, image_rect, image_x, image_y]

                #Agregar tiles a obstaculos
                if tile in obstaculos:
                    self.obstaculos_tiles.append(tile_data)

                #tile salida
                elif tile == 85:
                    self.exit_tile = tile_data

                    #crear monedas
                elif tile == 86:
                    moneda = Item(image_x, image_y, 0, item_imagenes[0])
                    self.lista_item.append(moneda)
                    tile_data[0] = tile_list[23]

                    #crear pociones
                elif tile == 89:
                    pocion = Item(image_x, image_y, 1, item_imagenes[1])
                    self.lista_item.append(pocion)
                    tile_data[0] = tile_list[23]

                    #crear enemigo_guardian
                elif tile == 74:
                    enemigo_guardian = personaje(image_x, image_y, animacion_enemigos[0], 300, 2)
                    self.lista_enemigo.append(enemigo_guardian)
                    tile_data[0] = tile_list[23]


                elif tile == 77:
                    guardian_esqueleto = personaje(image_x, image_y, animacion_enemigos[1], 200, 2)
                    self.lista_enemigo.append(guardian_esqueleto)
                    tile_data[0] = tile_list[23]

                self.map_tiles.append(tile_data)



    def update(self, posicion_pantalla):
        for tile in self.map_tiles:
            tile[2] += posicion_pantalla[0]
            tile[3] += posicion_pantalla[1]
            tile[1].center = (tile[2], tile[3])


    def draw(self, surface):
        for tile in self.map_tiles:
            surface.blit(tile[0], tile[1])