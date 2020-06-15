import pygame
from classes import LinkI
from config import FPS, vermelho, COMP, ALTU, GAME, QUIT
pygame.font.init ()


def initial_screen (window):
    clock = pygame.time.Clock()
    game=False
    inicio=True
    sheet_a=pygame.image.load ('img/sheet_a.png').convert_alpha()
    score_font = pygame.font.Font('fonte/PressStart2P.ttf', 28)
    score_font2=pygame.font.Font('fonte/PressStart2P.ttf', 15)
    linkin=pygame.sprite.Group()
    linki=LinkI(sheet_a)
    linkin.add (linki)
    while inicio:
        clock.tick (FPS)
        window.fill (vermelho)

        text_surface = score_font.render("{}".format("Sobrevivência do Link"), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (COMP / 2,  ALTU/2-100)
        window.blit(text_surface, text_rect)
        
        text_surface = score_font2.render("{}".format("Aperte espaço para começar"), True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (COMP / 2,  ALTU/2+50)
        window.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                inicio=False
                state=QUIT
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    inicio=False
                    state=GAME

        linkin.update()
        linkin.draw (window)
        pygame.display.update()
    return state