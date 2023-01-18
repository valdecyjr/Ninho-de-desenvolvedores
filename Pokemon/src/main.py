import pygame, sys, time
from scripts.button import Botao
import scripts.game as jogo
from scripts.message import box_message
pygame.init()


"""
    Classe onde vai ser configurado o meu jogo
"""
class Game:

    def __init__(self) -> None:
        """
            metodo da classe que inicia os parametros do meu jogo:
            tamanho da tela: self.size
            a tela: self.display
            e o tickrate: self.clock.tick
        """
        # configuraçoes inicias do jogo

        self.size = self.width, self.height = 1280, 704
        self.display = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Pokemon Ninho Dev')

        # carregando imagens e os criando botoes
        
        self.img_tela = pygame.image.load("imgs/tela_inicial/Tela_inicial.png")
        self.start_button = Botao('start',
                                  self.width-280,
                                  self.height*0.51,
                                  pygame.image.load('imgs/tela_inicial/start_button.png'))
        self.load_button = Botao('load',
                                 self.width-280,
                                 self.height*0.63,
                                 pygame.image.load('imgs/tela_inicial/load_button.png'))
        self.opcoes_button = Botao('opcoes',
                                   self.width-280,
                                   self.height*0.76,
                                   pygame.image.load('imgs/tela_inicial/opçoes_button.png'))
        self.quit_button = Botao('quit',
                                 self.width-280,
                                 self.height*0.87,
                                 pygame.image.load('imgs/tela_inicial/quit_button.png'))
        self.botoes_iniciais = [self.start_button, self.load_button, self.opcoes_button, self.quit_button]

    def run(self):
        """
            Metodo onde roda meu jogo
        """
        game_status = 'telainicial'
        while game_status != 'quit':
            size = self.display.get_size()
            self.img_tela = pygame.transform.scale(self.img_tela, size)
            mouse_cursor = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_status = 'quit'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_click = event.pos

                    if game_status == 'telainicial':
                        for i in range(len(self.botoes_iniciais)):
                            if self.botoes_iniciais[i].get_rect().collidepoint(mouse_click):
                                botao_pressionado = self.botoes_iniciais[i].name
                                game_status = botao_pressionado

            if game_status == 'telainicial':
                self.display.blit(self.img_tela, (0,0))
                self.start_button.draw_telainicial(size, 0.51)
                self.load_button.draw_telainicial(size, 0.63)
                self.opcoes_button.draw_telainicial(size, 0.76)
                self.quit_button.draw_telainicial(size, 0.87)

                for i in range(len(self.botoes_iniciais)):
                    for botoes in self.botoes_iniciais:
                        if botoes.get_rect().collidepoint(mouse_cursor):
                            pygame.draw.rect(self.display, (0,0,0), botoes.get_rect(),2)
                pygame.display.update()
            if game_status == 'start':
                jogo.game()
            elif game_status != 'telainicial' and game_status != 'quit':
                box_message('Ainda nao foi implementado', self.size[0]*0.3, self.size[1]/2)
                time.sleep(2)
                game_status = 'telainicial'


if __name__=='__main__':
    game = Game()
    game.run()