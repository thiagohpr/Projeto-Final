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
COMP_LINK=60
ALTU_LINK=55
COMP_INI=27
ALTU_INI=35

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
            image = pygame.Surface((sprite_width, sprite_height),pygame.SRCALPHA)
            image.convert_alpha()
            # Copia o sprite atual (do spritesheet) na imagem
            image.blit(spritesheet, (0, 0), dest_rect)
            sprites.append(image)
    return sprites

    
class Link (pygame.sprite.Sprite):
    def __init__(self,sheet):

        pygame.sprite.Sprite.__init__(self)
        
        sheet_m=pygame.transform.scale (sheet,(COMP_LINK*16,ALTU_LINK*2))
       
        spritesheet = load_spritesheet(sheet_m, 2, 18)

        self.animations = {
            Pcima: [spritesheet[0]],
            Pbaixo: [spritesheet[18]],
            Pdireita: [spritesheet[1]],
            Pesquerda: [spritesheet[19]],
            Acima: spritesheet[2:9],
            Abaixo: spritesheet[20:27],
            Adireita: spritesheet[10:17],
            Aesquerda: spritesheet[28:35],
        }
        # Define estado atual (que define qual animação deve ser mostrada)
        self.state = Pbaixo
        # Define animação atual
        self.animation = self.animations[self.state]
        # Inicializa o primeiro quadro da animação
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect=self.image.get_rect()

        self.rect.centerx=COMP/2
        self.rect.bottom=ALTU/2
        self.speedx=0
        self.speedy=0

        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 100

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

        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Atualiza animação atual
            self.animation = self.animations[self.state]
            # Reinicia a animação caso o índice da imagem atual seja inválido
            if self.frame >= len(self.animation):
                self.frame = 0
            
            # Armazena a posição do centro da imagem
            center = self.rect.center
            # Atualiza imagem atual
            self.image = self.animation[self.frame]
            # Atualiza os detalhes de posicionamento
            self.rect = self.image.get_rect()
            self.rect.center = center

class Inimigo (pygame.sprite.Sprite):
    def __init__ (self,imagem,link):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, COMP-COMP_INI )
        self.rect.y = random.randint(0, ALTU-ALTU_INI)
        self.speedx = 2
        self.speedy = 0

        self.link=link
        
    def update (self):
        centerx=self.link.rect.centerx
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left<=0 or self.rect.right>=COMP:
            self.speedx=-self.speedx




sheet_m=pygame.image.load ('C:/Users/thpro/Desktop/Desoft/Projeto-Final/sheet_m.png').convert_alpha()
inimigo_m=pygame.image.load ('C:/Users/thpro/Desktop/Desoft/Projeto-Final/linkfrente.png').convert()
link=Link(sheet_m)
inimigo=Inimigo(inimigo_m,link)
all_sprites=pygame.sprite.Group()
all_sprites.add (link)
all_sprites.add (inimigo)
game=True
clock = pygame.time.Clock()
FPS=60


while game:
    clock.tick (FPS)


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
                
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                link.speedx -= 2
                link.state=Aesquerda
            if event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                link.speedx += 2
                link.state=Adireita
            if event.key == pygame.K_UP or event.key==pygame.K_w:
                link.speedy -= 2
                link.state=Acima
            if event.key == pygame.K_DOWN or event.key==pygame.K_s:
                link.speedy += 2
                link.state=Abaixo
       
        if event.type == pygame.KEYUP:
           
            if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                link.speedx += 2
                link.state=Pesquerda
            if event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                link.speedx -= 2
                link.state=Pdireita
            if event.key == pygame.K_UP or event.key==pygame.K_w:
                link.speedy += 2
                link.state=Pcima
            if event.key == pygame.K_DOWN or event.key==pygame.K_s:
                link.speedy -= 2
                link.state=Pbaixo


    window.fill((0,0,0))
    window.blit (fundo,(0,0))
    all_sprites.update()
    all_sprites.draw(window)
    pygame.display.update()

pygame.quit()