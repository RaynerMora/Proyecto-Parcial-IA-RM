import pygame.sprite

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, item_type, animaciones_list):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type # 0 = monedas, 1 = posiones
        self.animaciones_list = animaciones_list
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animaciones_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect = (x,y)

    def update(self):
        cooldowm_animacion = 150 
        self.image = self.animaciones_list[self.frame_index]

        if pygame.time.get_ticks() - self.update_time > cooldowm_animacion:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animaciones_list):
            self.frame_index = 0