import pygame
import random

pygame.init ()



Pcima=0
Pbaixo=1
Pdireita=2
Pesquerda=3
Acima=4
Abaixo=5
Adireita=6
Aesquerda=7




COMP=514
ALTU=354
COMP_LINK=27
ALTU_LINK=35

window=pygame.display.set_mode((COMP,ALTU))
pygame.display.set_caption ("Jogo Fodinha")
fundo=pygame.image.load ('C:/Users/thpro/Desktop/Desoft/Projeto-Final/teste cenario.png').convert()
fundo=pygame.transform.scale (fundo,(COMP,ALTU))


def load_spritesheet(spritesheet, rows, columns):
    # Calcula a largura e altura de cada sprite.
    sprite_width = spritesheet.get_width() // columns
    sprite_height = spritesheet.get_height() // rows
    
    # Percorre todos os sprites adicionando em uma lista.
    sprites = []
    for row in range(rows):
        for column in range(columns):
            # Calcula posição do sprite atual
            x = column * sprite_width
            y = row * sprite_height
            # Define o retângulo que contém o sprite atual
            dest_rect = pygame.Rect(x, y, sprite_width, sprite_height)

            # Cria uma imagem vazia do tamanho do sprite
            image = pygame.Surface((sprite_width, sprite_height))
            # Copia o sprite atual (do spritesheet) na imagem
            image.blit(spritesheet, (0, 0), dest_rect)
            sprites.append(image)
    return sprites

    
class Link (pygame.sprite.Sprite):
    def __init__(self,sheet):

        pygame.sprite.Sprite.__init__(self)
        
        sheet_m=pygame.transform.scale (sheet_m,(COMP_LINK*16,ALTU_LINK*2))
        lista=load_spritesheet(sheet_m,2,16)
        

        self.rect=self.image.get_rect()
        self.rect.centerx=COMP/2
        self.rect.bottom=ALTU/2
        self.speedx=0
        self.speedy=0

    def update (self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy
 
        if self.rect.right > COMP:
            self.rect.right = COMP
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom>ALTU:
            self.rect.bottom=ALTU
        if self.rect.top<0:
            self.rect.top=0



sheet_m=pygame.image.load ('C:/Users/thpro/Desktop/Desoft/Projeto-Final/sheet_m.png')
link=Link(sheet_m)
all_sprites=pygame.sprite.Group()
all_sprites.add (link)
game=True
clock = pygame.time.Clock()
FPS=30


while game:
    clock.tick (FPS)


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
                
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                link.speedx -= 8
            if event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                link.speedx += 8
            if event.key == pygame.K_UP or event.key==pygame.K_w:
                link.speedy -= 8
            if event.key == pygame.K_DOWN or event.key==pygame.K_s:
                link.speedy += 8
       
        if event.type == pygame.KEYUP:
           
            if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                link.speedx += 8
            if event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                link.speedx -= 8
            if event.key == pygame.K_UP or event.key==pygame.K_w:
                link.speedy += 8
            if event.key == pygame.K_DOWN or event.key==pygame.K_s:
                link.speedy -= 8


    window.fill((0,0,0))
    window.blit (fundo,(0,0))
    all_sprites.update()
    all_sprites.draw(window)
    pygame.display.update()

pygame.quit()