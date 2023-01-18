import pygame


class Treinador(pygame.sprite.Sprite):
    def __init__(self, pos, groups, image) -> None:
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft = pos)
        self.direction =  pygame.math.Vector2()
        self.pokemons = []