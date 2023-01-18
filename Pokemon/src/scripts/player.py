import pygame, random
from scripts.db_read import db_select
from scripts.pokemon import Pokemon
from scripts.treinador import Treinador
from scripts.batalha import Batalha
from scripts.mochila import Mochila
from scripts.message import box_message

flag = None


# pokemons pelas rotas do mapa
route1 = ('Caterpie','Metapod', 'Weedle', 'Kakuna','Pidgey','Rattata')

class Player(Treinador):
    def __init__(self, pos, groups, obstacle_sprites, moitas) -> None:
        super().__init__(pos, groups, pygame.image.load("imgs/player_sprits/player_andandodireita2.png").convert_alpha())
        self.image = pygame.transform.scale(self.image,(48,48))
        self.speed = 2
        self.local = 'caucaiavillage'
        self.obstacle_sprites = obstacle_sprites
        self.moitas = moitas
        self.itens = {'pokebola': 6, 'reviver': 5, 'pocao': 3}
        self.step = 2
        self.proximo = 0
        self.batalha = 100
        self.animation = True
        self.mochilaflag = False
        self.pressx = False
        self.fim = True
        self.mochila = Mochila(self)
    
    def set_pokemon(self, pokemon):
        if len(self.pokemons) < 6:
            self.pokemons.append(pokemon)
        else:
            print('tem muitos pokemons')
    
    def update_pokemon(self):
        pass
                
        
    def encontrarPokemon(self, x):
        global flag
        if x != flag:
            batalhar = random.randint(0,1000)
            flag = x
            if batalhar < 200:
                name = random.choice(route1)
                pokemon_encontrado = Pokemon(db_select(name.lower()))
                batalha = Batalha(self, pokemon_encontrado, 'pokemon')
                self = batalha.new_player
                
    
    def pegarlocal(self):
        if self.rect.x < 1900 and self.rect.y < 1228:
            self.local = 'caucaiavillage'
        if (self.rect.x > 1900 and self.rect.x <= 2952) and (self.rect.y >= 640 and self.rect.y <= 1216):
            self.local = 'route1'

    def input(self):
        '''
        Função para input do teclado
        '''
        keys = pygame.key.get_pressed() # Retorna uma sequência de valores booleanos representando 
                                        # o estado de cada tecla do teclado como um dict

        if keys[pygame.K_LSHIFT]: # se a tecla left shift estiver pressionada
            self.speed = 4
        else:
            self.speed = 2
        
        if keys[pygame.K_SPACE]:
            self.mochilaflag = True

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
            self.image = pygame.image.load(f"imgs/player_sprits/player_andandocima{(self.step/6).__ceil__()}.png")
            self.image = pygame.transform.scale(self.image,(48,48))
            if self.step < 19 and self.animation == True:
                self.step += 1
                if self.step == 18:
                    self.animation = False
            elif self.step > 1 and self.animation == False:
                self.step -= 1
                if self.step == 1:
                    self.animation = True
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
            self.image = pygame.image.load(f"imgs/player_sprits/player_andandobaixo{(self.step/6).__ceil__()}.png")
            self.image = pygame.transform.scale(self.image,(48,48))
            if self.step < 19 and self.animation == True:
                self.step += 1
                if self.step == 18:
                    self.animation = False
            elif self.step > 1 and self.animation == False:
                self.step -= 1
                if self.step == 1:
                    self.animation = True
        else:
            if self.direction.y == 1:
                self.image = pygame.image.load("imgs/player_sprits/player_andandobaixo2.png")
                self.image = pygame.transform.scale(self.image,(48,48))
            elif self.direction.y == -1:
                self.image = pygame.image.load("imgs/player_sprits/player_andandocima2.png")
                self.image = pygame.transform.scale(self.image,(48,48))
            self.direction.y = 0

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.image = pygame.image.load(f"imgs/player_sprits/player_andandodireita{(self.step/6).__ceil__()}.png")
            self.image = pygame.transform.scale(self.image,(48,48))
            #animação
            if self.step < 19 and self.animation == True:
                self.step += 1
                if self.step == 18:
                    self.animation = False
            elif self.step > 1 and self.animation == False:
                self.step -= 1
                if self.step == 1:
                    self.animation = True
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.image = pygame.image.load(f"imgs/player_sprits/player_andandoesquerda{(self.step/6).__ceil__()}.png")
            self.image = pygame.transform.scale(self.image,(48,48))
            if self.step < 19 and self.animation == True:
                self.step += 1
                if self.step == 18:
                    self.animation = False
            elif self.step > 1 and self.animation == False:
                self.step -= 1
                if self.step == 1:
                    self.animation = True
        else:
            if self.direction.x == 1:
                self.image = pygame.image.load("imgs/player_sprits/player_andandodireita2.png")
                self.image = pygame.transform.scale(self.image,(48,48))
            elif self.direction.x == -1:
                self.image = pygame.image.load("imgs/player_sprits/player_andandoesquerda2.png")
                self.image = pygame.transform.scale(self.image,(48,48))
            self.direction.x = 0
    
    def move(self):
        """Função que movimenta o meu player"""

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * self.speed
        self.colisao('horizontal')
        self.rect.y += self.direction.y * self.speed
        self.colisao('vertical')


    def not_yet(self):
        display = pygame.display.get_surface()
        flag = True
        while flag:
            box_message('Fim de jogo, por enquanto', display.get_size()[0]*0.3,display.get_size()[1]*0.5)
            box_message('Press X para voltar ao jogo', display.get_size()[0]*0.3, display.get_size()[1]*0.8)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_x:
                        flag = False
    def colisao(self, direction):
        """Função responsavel por chegar as colisoes e as moitas"""
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                              
        for x, sprite in enumerate(self.moitas.sprites()):
            hitbox = self.rect.inflate(-12,-12)
            if sprite.hitbox.colliderect(hitbox):
                self.encontrarPokemon(x)

    def update(self):
        "função que faz meu player funcionar"
        self.input()
        if self.mochilaflag:
            self = self.mochila.draw()
        if self.fim:
            if self.rect.x >= 3436 and self.rect.y>=1448:
                self.not_yet()
                self.fim = False
        self.pegarlocal()
        self.move()


        1468