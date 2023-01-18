import pygame
from scripts.player import Player
from scripts.camera import CameraGroup
from scripts.getinfoimgs import *
from scripts.pokemon import Pokemon
from scripts.db_read import db_select
import scripts.tile as tile

class Map:
    """Classe que manipula meu mapa"""
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.tilesize = 64
        self.sprites_visiveis = CameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        self.moitas = pygame.sprite.Group()
        self.sprites_sheet_tileset = pygame.image.load('imgs/tileset/tileset.png').convert_alpha()
        self.intro = True
        self.create_map()
        self.clock = pygame.time.Clock()

    def create_map(self):
        '''desenha todo meu mapa'''
        tilesets = {
            'montanha': getinfo('imgs/mapas/worldmap_montanha.csv'),
            'agua': getinfo('imgs/mapas/worldmap_agua.csv'),
            'detalhes': getinfo('imgs/mapas/worldmap_detalhes.csv'),
            'casa': getinfo('imgs/mapas/worldmap_casa.csv'),
            'flores': getinfo('imgs\mapas\worldmap_flores.csv'),
            'estrada': getinfo('imgs/mapas/worldmap_estrada.csv'),
            'arvores': getinfo('imgs/mapas/worldmap_arvore.csv'),
            'moitas': getinfo('imgs/mapas/worldmap_moitas.csv')
        }
        for item, posicao in tilesets.items():
            for row_index, row in enumerate(posicao):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * self.tilesize
                        y = row_index * self.tilesize
                        if item == 'estrada':
                            tile.Tile((x,y),[self.sprites_visiveis], 'estrada', int(col))
                        if item == 'montanha':
                            tile.Tile((x,y),[self.sprites_visiveis, self.obstacles_sprites], 'montanha', int(col))
                        if item == 'moitas':
                            tile.Tile((x,y),[self.sprites_visiveis,self.moitas], 'moitas', int(col))
                        if item == 'casa':
                            y = (row_index+1)*self.tilesize
                            tile.Casa((x,y),[self.sprites_visiveis, self.obstacles_sprites], 'casa', int(col))
                        if item == 'agua':
                            tile.Tile((x,y),[self.sprites_visiveis], 'agua', int(col))
                        if item == 'detalhes':
                            tile.Tile((x,y),[self.sprites_visiveis, self.obstacles_sprites], 'detalhes', int(col))
                        if item == 'flores':
                            tile.Tile((x,y),[self.sprites_visiveis], 'flores', int(col))
                        if item == 'arvores':
                            tile.Tile((x,y),[self.sprites_visiveis, self.obstacles_sprites], 'arvores', int(col))
        self.player = Player((11*self.tilesize, 1*self.tilesize), [self.sprites_visiveis], self.obstacles_sprites, self.moitas)

    def run(self, pokemon=None):
        self.clock.tick(60)
        if self.intro:
            self.player.set_pokemon(Pokemon(db_select(pokemon)))
            self.intro = False
        self.sprites_visiveis.new_draw(self.player)
        self.sprites_visiveis.update()
