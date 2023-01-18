import pygame

def box_message(message,x ,y):
        """Função que recebe um texto e mostra ele na tela no posicao indicada"""

        display = pygame.display.get_surface()
        font = pygame.font.Font(pygame.font.get_default_font(), 30)
        text = font.render(message, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.x = x
        text_rect.y = y
        display.blit(text, text_rect)

        pygame.display.update()

def box_message2(message,eixo_x,eixo_y):
        """Função modificada que separa a msg por espaço"""
        texto = message.split()
        for i, variavel in enumerate(texto):
                display = pygame.display.get_surface()
                font = pygame.font.Font(pygame.font.get_default_font(), 30)
                text = font.render(variavel, True, (0,0,0))
                text_rect = text.get_rect()
                text_rect.x = eixo_x
                text_rect.y = eixo_y + (50*i)
                display.blit(text, text_rect)

        pygame.display.update()