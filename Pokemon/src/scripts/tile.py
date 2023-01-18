import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type,frame) -> None:
        super().__init__(groups)
        self.tilesize = 16
        self.sprite_type = sprite_type
        self.image = self.get_image(frame)
        self.rect = self.image.get_rect(topleft = pos)
        if self.sprite_type == 'moitas':
            self.hitbox = self.rect.inflate(-8,-8)


    def get_image(self,frame: int, img = pygame.image.load('imgs/tileset/agoravai.png')):
        if self.sprite_type == 'casa':
            img = pygame.image.load('imgs/tileset/build_tileset.png')
        width, height = 16, 16
        image = pygame.Surface((width, height))
        frame_y = (frame/14).__floor__()
        frame_x = frame - (frame_y*14)

        image.blit(img, (0,0), ( frame_x*16, (frame_y*16), width, height))
        image = pygame.transform.scale(image, (64, 64))
        image.set_colorkey((0,0,0))
        
        return image

class Casa(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type,arquivo) -> None:
        super().__init__(groups)
        self.image = pygame.image.load(f'imgs/tileset_buildings/{arquivo}.png').convert_alpha()
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (width*4, height*4))
        self.rect = self.image.get_rect(bottomleft = pos)
        self.image = pygame.transform.scale(self.image, (width*4, height*4))