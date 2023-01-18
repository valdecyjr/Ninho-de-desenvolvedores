import pygame, sys
from scripts.db_read import db_select
import scripts.map as map
from scripts.button import Botao
from scripts.message import box_message

args = db_select('charmander')
charmander_img = pygame.image.load(args[1])
args = db_select('bulbasaur')
bulbasaur_img = pygame.image.load(args[1])
args = db_select('squirtle')
squirtle_img = pygame.image.load(args[1])
charmander = Botao('charmander', 300, 250, charmander_img)
bulbasaur = Botao('bulbasaur', 600,250, bulbasaur_img)
squirtle = Botao('squirtle', 900, 250, squirtle_img)

pokemons = [charmander,bulbasaur, squirtle]





def game():
    world = pygame.display.get_surface()
    mapa = map.Map()
    game_status = 'select'
    while game_status != 'sair':
        size = world.get_size()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_status = 'sair'
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = event.pos

                if game_status == 'select':
                    for i in range(len(pokemons)):
                        if pokemons[i].get_rect().collidepoint(mouse_click):
                            pokemon_escolhido = pokemons[i]
                            game_status = 'start'
        if game_status == 'select':
            world.fill((255,255,255))
            charmander.draw_pokemons(size, 0.20)
            bulbasaur.draw_pokemons(size, 0.45)
            squirtle.draw_pokemons(size, 0.70)
            

            mouse_cursor = pygame.mouse.get_pos()
            for x,pokemon in enumerate(pokemons):
                if pokemon.get_rect().collidepoint(mouse_cursor):
                    pygame.draw.rect(world, (0,0,0), pokemon.get_rect(),2)
            
            box_message('Escolha seu pokemon inicial', (world.get_size()[0]*0.26),(world.get_size()[1]*0.24))
            pygame.display.update()
            

        if game_status == 'start':
            world.fill((0,0,0))
            mapa.run(pokemon_escolhido.name)
            pygame.display.update()