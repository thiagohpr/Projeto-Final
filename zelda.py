import pygame
from initial_screen import initial_screen
from game_screen import game_screen
from over_screen import over_screen
from config import COMP, ALTU, INICIO, GAME, FIM, QUIT
pygame.init ()
pygame.mixer.init()

window=pygame.display.set_mode((COMP,ALTU))
pygame.display.set_caption ("Sobrevivência")
pygame.mixer.music.load('som/saria.wav')
pygame.mixer.music.set_volume(0.3)

pygame.mixer.music.play(loops=-1)

score=0
state = INICIO
while state != QUIT:
    if state == INICIO:
        state = initial_screen(window)
    elif state == GAME:
        state,score = game_screen(window)
    elif state == FIM:
        state = over_screen(window, score)
    else:
        state = QUIT
pygame.quit()