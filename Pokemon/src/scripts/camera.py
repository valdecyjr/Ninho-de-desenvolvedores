import pygame, csv

class CameraGroup(pygame.sprite.Group):
    """
    Grupo de sprites que vao ser visivel pela camera
    Vou classificar os sprites pela ordenada Y
    """
    def __init__(self) -> None:
        super().__init__()
        self.display = pygame.display.get_surface()
        self.camera_width = self.display.get_size()[0] // 2
        self.camera_height = self.display.get_size()[1] // 2 
        self.deslocamento = pygame.math.Vector2(0, 0)
        # chao
        self.floor_image = pygame.image.load('imgs/mapas/mapa1.png')
        width, height = self.floor_image.get_size()
        self.floor_image = pygame.transform.scale(self.floor_image,(width*4,height*4))
        self.floor_rect = self.floor_image.get_rect(topleft = (0,0))


    def new_draw(self, player):
        # setando o meio da camera
        self.deslocamento.x = player.rect.centerx - self.camera_width
        self.deslocamento.y = player.rect.centery - self.camera_height

        #desenhando o chao
        floor_deslocamento_pos = self.floor_rect.topleft - self.deslocamento
        self.display.blit(self.floor_image, floor_deslocamento_pos)
        #desenhar meus sprites
        for sprites in self.sprites():
            deslocamento_pos = sprites.rect.topleft - self.deslocamento
            self.display.blit(sprites.image,deslocamento_pos)