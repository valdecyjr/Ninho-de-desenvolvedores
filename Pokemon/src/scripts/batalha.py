import pygame,sys, random, math, time
from scripts.button import Botao
from scripts.message import box_message


class Batalha():
    '''Classe que fica todo meu sistema de batalha'''
    def __init__(self,player,inimigo,tipo_inimigo) -> None:
        self.display = pygame.display.get_surface()
        self.player = player
        self.pokemon_batalha = None
        self.inimigo = inimigo
        # tipo de inimigo, pokemon ou um npc
        self.tipo = tipo_inimigo 
        # controla os turnos da minha batalha
        self.batalha = 'pre batalha' 
        # variavel para ajudar a controlar o turno do player
        self.player_turn = 'inicio' 
        self.intro = True
        self.new_player = self.run()

    def escolher_pokemon(self, txt):
        """função que permite voce escolher o pokemon para batalha"""

        # parametros iniciais
        aux, i = 0, len(self.player.pokemons)
        click = []
        x, y = self.display.get_size()
        x ,y = x*0.2, y*0.2
        pokemons = []
        # setar meus botoes

        for i in range(len(self.player.pokemons)):
                if i < 3:
                    new_x = x + 250*i
                    new_y = y
                else:
                    new_x = x + (250*(i-3))
                    new_y = y + 200

                pokemons.append(Botao(self.player.pokemons[i].nome,
                                      new_x,
                                      new_y,
                                      self.player.pokemons[i].image))

        # While que desenha minha tela
        while True:
            self.display.fill((255,255,255))

            mouse_cursor = pygame.mouse.get_pos()

            # Desenha meus botoes
            for pokemon in pokemons:
                pokemon.draw_pokemons()

            # desenha um quadrado no botao que o mouse se encontra
            for x,pokemon in enumerate(pokemons):
                    if pokemon.get_rect().collidepoint(mouse_cursor):
                        pygame.draw.rect(self.display, (0,0,0), pokemon.get_rect(),2)

            #pega todos os eventos na minha tela(clicks e botoes pressionados)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                
                    mouse_click = event.pos

                    for x, pokemon in enumerate(pokemons):
                        if pokemon.get_rect().collidepoint(mouse_click):
                            
                            for objetos in self.player.pokemons:
                                if objetos not in click:
                                    if pokemon.name == objetos.nome:
                                        if aux <= i:
                                            if objetos.stats['hp'] > 0:
                                                return objetos
                                            else:
                                                box_message(f'{objetos.nome} nao tem hp suficiente', x*0.2, y*0.66)
                                                click.append(objetos)
                                                time.sleep(2)
                                                aux +=1
                                elif objetos in click and aux>i:
                                    box_message('Não tem pokemons disponivel para batalhar', x*0.2, y*0.66)
                                    time.sleep(2)
                                    return None
                                else:
                                    box_message(f'{objetos.nome} ja tentou escolher', x*0.2, y*0.66)
                                    time.sleep(2)

            box_message(txt, (self.display.get_size()[0]*0.2), 50)
            pygame.display.update()
    
    def create_buttons(self, width, height, left, top, text_cx, text_cy,label):
        mouse_curso = pygame.mouse.get_pos()
        button = pygame.Rect(left, top, width, height)
        if button.collidepoint(mouse_curso):
            pygame.draw.rect(self.display, (255,223,0), button)
        else:
            pygame.draw.rect(self.display, (255,255,255), button)
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render(f'{label}', True, (0,0,0))
        text_rect = text.get_rect(center = (text_cx, text_cy))
        self.display.blit(text, text_rect)

        return button

    def draw_hp(self,pokemon,x,y):
        hp = pokemon.stats['hp']
        max_hp = pokemon.stats['max_hp']
        bar_scale = 200 // max_hp

        # desenha uma rect na cor vermelha
        for i in range(max_hp):
            bar = (x + bar_scale * i, y, bar_scale, 20)
            pygame.draw.rect(self.display, (255,0,0), bar)
        
        # desenha um rect na cor verde
        for i in range(hp):
            bar = (x + bar_scale * i, y, bar_scale, 20)
            pygame.draw.rect(self.display, (0,255,0), bar)

        # imprimi a quantidade de hp na tela
        font = pygame.font.Font(pygame.font.get_default_font(),16)
        text = font.render(f'HP: {hp} / {max_hp} ' ,True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.x = x
        text_rect.y = y
        self.display.blit(text, text_rect)



    def run(self):
        ''' Função onde vai rodar toda a logica da minha batalha'''
        # pega o pokemon que voce escolheu 
        self.pokemon_batalha = self.escolher_pokemon('Escolha o pokemon para batalhar')
        while self.batalha != 'fim':
            x, y = self.display.get_size()
            #  toda a entrada de dados acontece aqui
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_click = event.pos
                    if self.batalha == 'turno do player':
                        if self.player_turn == 'inicio':
                            if fight_button.collidepoint(mouse_click):
                                self.player_turn = 'fight'
                            if itens_button.collidepoint(mouse_click):
                                self.player_turn = 'itens'
                            if escape_button.collidepoint(mouse_click):
                                self.batalha = 'fim'
                        elif self.player_turn == 'fight':
                            if ataque_button.collidepoint(mouse_click):
                                if self.tipo == 'pokemon':
                                    ataque = player_ataque - inimigo_defesa
                                    if ataque > 0:
                                        self.inimigo.stats['hp'] -= ataque
                                self.batalha = 'turno do adversario'
                            if habilidades_button.collidepoint(mouse_click):
                                self.player_turn = 'habilidade'
                            if voltar_button.collidepoint(mouse_click):
                                self.player_turn = 'inicio'
                        elif self.player_turn == 'itens':
                            for i in range(len(itens_buttons)):
                                if itens_buttons[i].collidepoint(mouse_click):
                                    for key in self.player.itens.keys():
                                        if keys[i] and key == 'pocao':
                                            self.pokemon_batalha.stats['hp'] += 50
                                            if self.pokemon_batalha.stats['hp'] > max_hp_player:
                                                self.pokemon_batalha.stats['hp'] = max_hp_player
                                            self.player.itens['pocao'] -= 1
                                        else:
                                            box_message('Ainda nao foi implementado',x, y)
                                            time.sleep(1)
                                            self.player_turn = 'inicio'
                            if voltar_button.collidepoint(mouse_click):
                                self.player_turn = 'inicio'

                        elif self.player_turn == 'habilidade':
                            for i in range(len(move_buttons)):
                                if move_buttons[i].collidepoint(mouse_click):
                                    if self.pokemon_batalha.moves_mp[i] > 0:
                                        self.pokemon_batalha.moves_mp[i] -= 1
                                        ataque = math.floor(self.pokemon_batalha.moves_power[i])
                                        if self.tipo == 'pokemon':
                                            ataque -= inimigo_defesa
                                            if ataque > 0:
                                                self.inimigo.stats['hp'] -= ataque
                                            else:
                                                box_message(f'{self.pokemon_batalha.nome} errou', x*0.2, y*0.66)
                                                time.sleep(2)
                                    else:
                                        box_message('Voce nao tem mp suficiente', x*0.2, y*0.66)
                                        time.sleep(2)
                                    self.player_turn = 'inicio'

                            if voltar_button2.collidepoint(mouse_click):
                                self.player_turn = 'fight'
                    elif self.batalha == 'capturar':
                        if sim_button.collidepoint(mouse_click):
                            self.batalha = 'sim'
                        if nao_button.collidepoint(mouse_click):
                            self.batalha = 'nao'

            # acaba a entrada de dados e começa a logica da batalha

            # checa o hp dos dois pokemons em batalha
            if self.tipo == 'pokemon':
                if self.pokemon_batalha == None:
                    box_message('Voce perdeu', x/2 , y/2)
                    time.sleep(2)
                    break

                elif self.pokemon_batalha.stats['hp'] <= 0:
                    self.pokemon_batalha.stats['hp'] = 0
                    box_message(f'{self.pokemon_batalha.nome} desmaoiu',x*0.2, y*0.66)
                    time.sleep(2)
                    self.pokemon_batalha = self.escolher_pokemon('Escolha outro pokemon para batalhar')
                    self.batalha = 'pre batalha'        
                elif self.inimigo.stats['hp'] <= 0:
                    self.inimigo.stats['hp'] = 0
                    if self.batalha != 'capturar' and self.batalha != 'sim' and self.batalha != 'nao':
                        self.batalha = 'capturar'

            #  Aqui começa os turnos da batalha

            # Animação inicial da batalha
            if self.batalha == 'pre batalha':
                if self.tipo == 'pokemon':
                    self.display.fill((255,255,255))
                    pygame.draw.rect(self.display, (0,0,0),(0, y*0.65, x*0.19, y), 3)
                    pygame.draw.rect(self.display, (0,0,0),(0, y*0.65, x, y), 3)
                    self.display.blit(self.inimigo.image,(x*0.55,y*0.08))
                    if self.intro:
                        box_message(f'Voce encontrou um {self.inimigo.nome}', x*0.2, y*0.66)
                        time.sleep(2)
                        self.intro = False
                    self.display.fill((255,255,255))
                    pygame.draw.rect(self.display, (0,0,0),(0, y*0.65, x*0.19, y), 3)
                    pygame.draw.rect(self.display, (0,0,0),(0, y*0.65, x, y), 3)
                    self.display.blit(self.inimigo.image,(x*0.55,y*0.08))
                    self.display.blit(self.pokemon_batalha.image, (x*0.24,y*0.36))
                    box_message(f'Vai, {self.pokemon_batalha.nome}', x*0.2, y*0.66)
                    time.sleep(2)
                
                self.batalha = 'setar_batalha'
            # Começa a batalha

            else:
                self.display.fill((255,255,255))
                self.display.blit(self.pokemon_batalha.image, (x*0.24,y*0.36))
                self.draw_hp(self.pokemon_batalha, x*0.24,y*0.29)
                if self.tipo == 'pokemon':
                    self.draw_hp(self.inimigo, x*0.55, 0)
                    self.display.blit(self.inimigo.image,(x*0.55,y*0.08))

                    # setar os danos as defesas e quem começa
                    if self.batalha == 'setar_batalha':
                        player_ataque = math.floor(self.pokemon_batalha.stats['defesa']*0.7)
                        player_defesa = math.floor(self.pokemon_batalha.stats['defesa']*0.5)
                        inimigo_ataque = math.floor(self.inimigo.stats['ataque']*0.7)
                        inimigo_defesa = math.floor(self.inimigo.stats['defesa']*0.5)
                        max_hp_inimigo = self.inimigo.stats['hp']
                        max_hp_player = self.pokemon_batalha.stats['hp']
                        if self.inimigo.stats['speed'] > self.pokemon_batalha.stats['speed']:
                            self.batalha = 'turno do adversario'
                        else:
                            self.batalha = 'turno do player'

                elif self.tipo == 'npc':
                    pass
                # Turno do adversario
                if self.batalha == 'turno do adversario':
                    pygame.draw.rect(self.display, (0,0,0),(0, y*0.65, x*0.19, y), 3)
                    pygame.draw.rect(self.display, (0,0,0),(0, y*0.65, x, y), 3)
                    if self.tipo == 'pokemon':
                        opcao = random.randint(1, 2)
                        if opcao == 1:
                            ataque = inimigo_ataque - player_defesa
                        else:
                            movimento = random.choice(self.inimigo.moves_aprendidos)
                            for x in range(len(self.inimigo.moves_aprendidos)):
                                if movimento == self.inimigo.moves_aprendidos[x]:
                                    i = x
                            ataque = self.inimigo.moves_power[i]                                    
                            ataque -= player_defesa

                        if ataque > 0:
                            if opcao == 1:
                                box_message(f'{self.inimigo.nome} efetuo um etaque', x*0.2, y*0.66)
                            else:
                                box_message(f'{self.inimigo.nome} usou a habilidade {movimento}', x*0.2, y*0.66)

                            self.pokemon_batalha.stats['hp'] = math.floor(self.pokemon_batalha.stats['hp']- ataque)

                        else:
                            box_message(f'{self.inimigo.nome} errou o ataque', x*0.2, y*0.66)

                    
                    self.batalha = 'turno do player'
                    self.player_turn = 'inicio'
                    time.sleep(2)

                # turno do player
                if self.batalha == 'turno do player':
                    # desenha botoes iniciais ( fight,itens e escape)
                    if self.player_turn == 'inicio':
                        fight_button = self.create_buttons(x*0.19,y*0.1, 0, y*0.65, (x*0.11)-10, y*0.7, 'Fight')
                        itens_button = self.create_buttons(x*0.19,y*0.1, 0, y*0.78, (x*0.11)-10, y*0.82, 'Itens')
                        escape_button = self.create_buttons(x*0.19, y*0.1, 0, y*0.91, (x*0.11)-10, y*0.94, 'Escapar')
                    # desenha as opçoes caso aperte fight
                    elif self.player_turn == 'fight':
                        ataque_button = self.create_buttons(x*0.19,y*0.1, 0, y*0.65, (x*0.11)-10, y*0.7, 'Ataque')
                        habilidades_button = self.create_buttons(x*0.19,y*0.1, 0, y*0.78, (x*0.11)-10, y*0.82, 'Habilidades')
                        voltar_button = self.create_buttons(x*0.19, y*0.1, 0, y*0.91, (x*0.11)-10, y*0.94, 'Voltar')
                    # desenha as opcoes caso aperte itens
                    elif self.player_turn == 'itens':
                        voltar_button = self.create_buttons(x*0.19, y*0.1, 0, y*0.91, (x*0.11)-10, y*0.94, 'Voltar')
                        itens_buttons = []
                        keys = []

                        for i, key in enumerate(self.player.itens.keys()):
                            item = key
                            button_width = x*0.19
                            button_height = y*0.1
                            if i == 0 or i == 2:
                                left = x*0.2 + i % 2 * button_width
                            else:
                                left = x*0.4 + i % 2 * button_width
                            if i == 0 or i == 1:
                                top = y*0.70 + i // 2 * button_height
                            else:
                                top = y*0.8 + i // 2 * button_height
                            text_center_x =  left+ 120
                            text_center_y = top + 35
                            button = self.create_buttons(button_width, button_height, left, top, text_center_x, text_center_y, item)
                            keys.append(item)
                            itens_buttons.append(button)

                    # se em figth escolheu usar uma habilidade
                    elif self.player_turn == 'habilidade':
                        voltar_button2 = self.create_buttons(x*0.19, y*0.1, 0, y*0.91, (x*0.11)-10, y*0.94, 'Voltar')
                        move_buttons = []
                        
                        for i in range(len(self.pokemon_batalha.moves_aprendidos)):
                            move = f'{self.pokemon_batalha.moves_aprendidos[i]}:{self.pokemon_batalha.moves_mp[i]}'
                            button_width = x*0.19
                            button_height = y*0.1
                            if i == 0 or i == 2:
                                left = x*0.2 + i % 2 * button_width
                            else:
                                left = x*0.4 + i % 2 * button_width
                            if i == 0 or i == 1:
                                top = y*0.70 + i // 2 * button_height
                            else:
                                top = y*0.8 + i // 2 * button_height
                            text_center_x =  left+ 120
                            text_center_y = top + 35
                            button = self.create_buttons(button_width, button_height, left, top, text_center_x, text_center_y, move)
                            move_buttons.append(button)
                    pygame.draw.rect(self.display, (0,0,0),(0, y*0.65, x*0.19, y), 3)
                    pygame.draw.rect(self.display, (0,0,0),(0, y*0.65, x, y), 3)
                elif self.batalha == 'capturar':
                    self.pokemon_batalha.xp += 20 * self.pokemon_batalha.level
                    sim_button = self.create_buttons(x*0.19,y*0.1,(x/2)-(x*0.19),(y/2)-(y*0.1),(x/2)-(x*0.095),(y/2)-(y*0.05),'Sim')
                    nao_button = self.create_buttons(x*0.19,y*0.1,(x/2),(y/2)-(y*0.1),(x/2)+(x*0.095),(y/2)-(y*0.05),'Nao')
                    box_message(f'Voce deseja capturar {self.inimigo.nome}?',(x/2)-(x*0.19),(y/2)-(y*0.1)-50)
                
                # Caso escolheu sim no captura
                elif self.batalha == 'sim':
                    if self.player.itens['pokebola'] > 0 and len(self.player.pokemons) < 6:
                        self.inimigo.stats['hp'] = max_hp_inimigo
                        self.player.set_pokemon(self.inimigo)
                        self.player.itens['pokebola'] -= 1
                        box_message(f'Voce capturou {self.inimigo.nome} com sucesso',(x/2)-(x*0.19),(y/2)-(y*0.1)-50)
                        time.sleep(2)
                        break
                    elif len(self.player.pokemons)>5:
                        box_message(f'Voce ja tem muitos pokemons',(x/2)-(x*0.19),(y/2)-(y*0.1)-50)
                        time.sleep(2)
                        break
                    else:
                        box_message('Voce nao tem pokebola',(x/2)-(x*0.19),(y/2)-(y*0.1)-50)
                        time.sleep(2)
                        break
                # se escolheu nao so finaliza
                elif self.batalha == 'nao':
                    break
            pygame.display.update()
        return self.player