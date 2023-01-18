import pygame, sys
from scripts.button import Botao
from scripts.message import box_message2

class Mochila():
    '''Classe que desenha a mochila do player'''
    def __init__(self, player) -> None:
        self.screen = pygame.display.get_surface()
        self.x = 0
        self.y = self.screen.get_size()[1]*0.2
        self.size = (self.x, self.y)
        self.image = pygame.image.load('imgs/tela_inicial/mochila.png')
        self.opcao = 'nada'
        self.player = player

    def pokemon_stats(self, pokemon):
        flag = True
        moves = ''
        for habilidade in pokemon.moves_aprendidos:
            moves += f' {habilidade}'

            txt =f"""
            nome:{pokemon.nome}
            level:{pokemon.level}
            xp:{pokemon.xp}
            tipo:{pokemon.tipo}
            status:
                ataque:{pokemon.stats['ataque']}
                defesa:{pokemon.stats['defesa']}
                ataque_especial:{pokemon.stats['ataque_especial']}
                defesa_especial:{pokemon.stats['defesa_especial']}
                max_hp:{pokemon.stats['max_hp']}
                hp:{pokemon.stats['hp']}
                speed:{pokemon.stats['speed']}
            """
            txt2 = f"""
            habilidades_aprendidas:
                {moves}
            """

        while flag:
            self.screen.fill((255,255,255))
            sprite = pokemon.image
            pygame.draw.rect(self.screen,(0,0,0),sprite.get_rect(),3)
            self.screen.blit(sprite, (0,0))

            box_message2(txt, 200,0)
            box_message2(txt2,500,0)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_x:
                        self.opcao = 'nada'
                        flag = False
            pygame.display.update()

    def drawpokemons(self):
        x = 250
        y = self.y
        pokemons = []
        tela_pokemon = pygame.Rect(x,y,800,340,)
        pygame.draw.rect(self.screen,(255,255,255), tela_pokemon)


        for i in range(len(self.player.pokemons)):
            if i < 3:
                new_x = x + 250*i
                new_y = self.y
            else:
                new_x = x + (250*(i-3))
                new_y = self.y + 200

            pokemons.append(Botao(self.player.pokemons[i].nome,
                                  new_x,
                                  new_y,
                                  self.player.pokemons[i].image))


        mouse_cursor = pygame.mouse.get_pos() 
        for pokemon in pokemons:
            pokemon.draw_pokemons()


        for x,pokemon in enumerate(pokemons):
                if pokemon.get_rect().collidepoint(mouse_cursor):
                    pygame.draw.rect(self.screen, (0,0,0), pokemon.get_rect(),2)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_x:
                    self.aux = None
                    self.opcao = 'nada'
                    self.player.mochilaflag = False
                    return self.player

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_click = event.pos

                if self.pokemons_button.collidepoint(mouse_click):
                    self.opcao = 'pokemons'

                if self.itens_button.collidepoint(mouse_click):
                    self.opcao = 'itens'

                if self.sair_button.collidepoint(mouse_click):
                    self.opcao = 'nada'
                    self.player.mochilaflag = False
                    return self.player

                for i in range(len(pokemons)):
                    if pokemons[i].get_rect().collidepoint(mouse_click):
                        for objetos in self.player.pokemons:
                            if pokemons[i].name == objetos.nome:
                                self.pokemon_stats(objetos)
    
    def drawitens(self):
        x = 250
        y = self.y
        itens = []
        tela_itens = pygame.Rect(x,y,750,340,)
        pygame.draw.rect(self.screen,(255,255,255), tela_itens)

        for i,key in enumerate(self.player.itens.keys()):
            if i < 3:
                new_x = x + 250*i
                new_y = self.y
            else:
                new_x = x + (250*(i-3))
                new_y = self.y + 150
            value = self.player.itens[key]
            itens.append(self.create_buttons(200,30,new_x,new_y,new_x+100, new_y+15, f"{key}:{value}",(255,255,255)))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_x:
                    self.opcao = 'nada'
                    self.player.mochilaflag = False
                    return self.player

            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_click = event.pos

                if self.pokemons_button.collidepoint(mouse_click):
                    self.opcao = 'pokemons'

                if self.itens_button.collidepoint(mouse_click):
                    self.opcao = 'itens'

                if self.sair_button.collidepoint(mouse_click):
                    self.opcao = 'nada'
                    self.player.mochilaflag = False
                    return self.player

    def draw(self):
        sprite = self.image.copy()
        transparencia = (255,255,255,255)
        sprite.fill(transparencia, None, pygame.BLEND_RGBA_MULT)
        self.screen.blit(sprite, self.size)
        self.pokemons_button = self.create_buttons(200,30,10,self.y+20,100,self.y+35, 'pokemons')
        self.itens_button = self.create_buttons(200,30,10,self.y+55,100,self.y+70, 'itens')
        self.pokedex_button = self.create_buttons(200,30,10,self.y+90,100,self.y+105, 'pokedex')
        self.sair_button = self.create_buttons(200,30,10,self.y+300,105,self.y+315, 'sair')
        
        if self.opcao == 'pokemons':
            self.drawpokemons()

        if self.opcao == 'itens':
            self.drawitens()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = event.pos

                if self.pokemons_button.collidepoint(mouse_click):
                    self.opcao = 'pokemons'

                if self.itens_button.collidepoint(mouse_click):
                    self.opcao = 'itens'

                if self.sair_button.collidepoint(mouse_click):
                    self.opcao = 'nada'
                    self.player.mochilaflag = False
                    return self.player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    self.opcao = 'nada'
                    self.player.mochilaflag = False
                    return self.player
        return self.player
    
    def create_buttons(self, width, height, left, top, text_cx, text_cy,label, color = (195,195,195) ):
        mouse_curso = pygame.mouse.get_pos()
        button = pygame.Rect(left, top, width, height)
        if button.collidepoint(mouse_curso):
            pygame.draw.rect(self.screen, (255,223,0), button)
        else:
            pygame.draw.rect(self.screen, color, button)
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        text = font.render(f'{label}', True, (0,0,0))
        text_rect = text.get_rect(center = (text_cx, text_cy))
        self.screen.blit(text, text_rect)

        return button

