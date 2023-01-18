import pygame


class Botao(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img) -> None:
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.size = (self.x, self.y)
        self.image = img

    def draw_telainicial(self, size=None,porc = None):
        screen = pygame.display.get_surface()
        sprite = self.image.copy()
        transparencia = (255,255,255,255)
        sprite.fill(transparencia, None, pygame.BLEND_RGBA_MULT)
        if size is not None and porc is not None:
            self.x, self.y = size
            self.x, self.y = self.x - 280, self.y*porc
            self.size = self.x, self.y
        screen.blit(sprite, self.size)

    def draw_pokemons(self, size=None,porc = None):
        screen = pygame.display.get_surface()
        sprite = self.image.copy()
        transparencia = (255,255,255,255)
        sprite.fill(transparencia, None, pygame.BLEND_RGBA_MULT)
        if size is not None and porc is not None:
            self.x, self.y = size
            self.x, self.y = self.x * porc, self.y * 0.4
            self.size = self.x, self.y
        screen.blit(sprite, self.size)
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())