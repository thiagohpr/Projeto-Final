import pygame
import random
from config import Pcima, Pbaixo, Pdireita, Pesquerda, Acima, Abaixo,Adireita, Aesquerda, COMP_LINK, ALTU_LINK, COMP, ALTU, COMP_LAVA, ALTU_LAVA

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
        self.last_update2 = pygame.time.get_ticks()
        self.frame_ticks = 100
        self.frame_ticks2=1
        self.hitbox=pygame.Rect(self.rect.x+15,self.rect.y+12,COMP_LINK-35,ALTU_LINK-23)
        self.poder=0
        self.posx=self.rect.x
        self.posy=self.rect.y


    def update (self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
 
        if self.rect.right > 10+COMP:
            self.rect.right = 10+COMP
        if self.rect.left < -15:
            self.rect.left = -15

        if self.rect.bottom>10+ALTU:
            self.rect.bottom=10+ALTU
        if self.rect.top<30:
            self.rect.top=30
        

        if self.speedx>0:
            self.state=Adireita
            self.hitbox=pygame.Rect(self.rect.x+35,self.rect.y+14,COMP_LINK-48,ALTU_LINK-33)
        elif self.speedx<0:
            self.state=Aesquerda
            self.hitbox=pygame.Rect(self.rect.x+28,self.rect.y+16,COMP_LINK-49,ALTU_LINK-34)
        if self.speedy>0:
            self.state=Abaixo
            self.hitbox=pygame.Rect(self.rect.x+23,self.rect.y+19,COMP_LINK-47,ALTU_LINK-34)
        elif self.speedy<0:
            self.state=Acima
            self.hitbox=pygame.Rect(self.rect.x+23,self.rect.y+12,COMP_LINK-46,ALTU_LINK-35)

        if self.state==Pdireita:
            self.hitbox=pygame.Rect(self.rect.x+22,self.rect.y+15,COMP_LINK-49,ALTU_LINK-32)
        elif self.state==Pesquerda:
            self.hitbox=pygame.Rect(self.rect.x+21,self.rect.y+15,COMP_LINK-50,ALTU_LINK-31)
        elif self.state==Pbaixo:
            self.hitbox=pygame.Rect(self.rect.x+18,self.rect.y+16,COMP_LINK-44,ALTU_LINK-31)
        elif self.state==Pcima:
            self.hitbox=pygame.Rect(self.rect.x+18,self.rect.y+15,COMP_LINK-45,ALTU_LINK-33)

        

        now = pygame.time.get_ticks()
        if now==self.last_update2:
            self.posx=self.rect.x
            self.posy=self.rect.y

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update
        elapsed_ticks2 = now - (self.last_update2)
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

        if elapsed_ticks2 > self.frame_ticks2:
            self.last_update2 = now

            self.posx2=self.rect.x
            self.posy2=self.rect.y
            if (self.posx2-self.posx)**2>0 or (self.posy2-self.posy)**2>0:
                self.poder=0.5
            else:
                self.poder=0
            self.posx=self.posx2
            self.posy=self.posy2



class Flecha (pygame.sprite.Sprite):
    def __init__ (self,link,imagem):
        pygame.sprite.Sprite.__init__(self)
        if link.state==Pdireita or link.state==Adireita:
            self.image=imagem[0]
            self.rect=self.image.get_rect()
            self.rect.centerx=link.rect.centerx+20
            self.rect.centery=link.rect.centery
            self.speedx=4
            self.speedy=0


        if link.state==Pesquerda or link.state==Aesquerda:
            self.image=imagem[1]
            self.rect=self.image.get_rect()
            self.rect.centerx=link.rect.centerx-20
            self.rect.centery=link.rect.centery
            self.speedx=-4
            self.speedy=0


        if link.state==Pcima or link.state==Acima:
            self.image=imagem[2]
            self.rect=self.image.get_rect()
            self.rect.centerx=link.rect.centerx
            self.rect.centery=link.rect.centery-20
            self.speedx=0
            self.speedy=-4


        if link.state==Pbaixo or link.state==Abaixo:
            self.image=imagem[3]
            self.rect=self.image.get_rect()
            self.rect.centerx=link.rect.centerx
            self.rect.centery=link.rect.centery+20
            self.speedx=0
            self.speedy=4
        
    def update (self):
        self.rect.centerx+=self.speedx
        self.rect.centery+=self.speedy

        
class LinkI (pygame.sprite.Sprite):
    def __init__ (self,sheet):
        pygame.sprite.Sprite.__init__(self)

        sheet_a=pygame.transform.scale (sheet,(COMP_LINK*27,ALTU_LINK*4))
        self.spritesheet = load_spritesheet(sheet_a, 1, 8)
        self.frame = 0
        self.image = self.spritesheet[self.frame]
        self.rect=self.image.get_rect()
        self.rect.centerx=COMP/2
        self.rect.bottom=230
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 100
    def update (self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1
            if self.frame >= len(self.spritesheet):
                self.frame = 0
            center = self.rect.center
            self.image = self.spritesheet[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center
        
    
class Inimigo (pygame.sprite.Sprite):
    def __init__ (self,link,sheet):
        pygame.sprite.Sprite.__init__(self)
        

        self.speedx = 2
        self.speedy = 0

        self.link=link
        
        sheet_i=pygame.transform.scale (sheet,(COMP_LINK*2,ALTU_LINK*3))
        spritesheet = load_spritesheet(sheet_i, 4, 4)

        self.animations = {
            Acima: spritesheet[12:15],
            Abaixo: spritesheet[0:3],
            Adireita: spritesheet[4:7],
            Aesquerda: spritesheet[8:11],
        }

        self.state = Adireita
        self.animation = self.animations[self.state]
        
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect=self.image.get_rect()
        self.rect.x = random.randint (0,COMP-COMP_LINK)
        self.rect.y = random.randint (40,ALTU-ALTU_LINK)

        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 150

        self.hitbox=pygame.Rect(self.rect.x+7,self.rect.y+3,COMP_LINK-34,ALTU_LINK-15)
    def update (self):
        
        centerxl=self.link.rect.centerx
        centeryl=self.link.rect.centery
        centerx=self.rect.centerx 
        centery=self.rect.centery

        direita=abs(self.rect.right-self.link.rect.left)
        esquerda=abs(self.rect.left-self.link.rect.right)
        cima=abs(self.rect.top-self.link.rect.bottom)
        baixo=abs(self.rect.bottom-self.link.rect.top)
        if (((centerx-centerxl)**2)<25000) and (((centery-centeryl))**2<25000):
            if abs(centerxl)-abs(centerx)<3 and centeryl-centery>0:
                self.state=Abaixo
            elif abs(centerxl)-abs(centerx)<3 and centeryl-centery<0:
                self.state=Acima
            elif abs(centeryl)-abs(centery)<3 and centerxl-centerx>0:
                self.state=Adireita
            elif abs(centeryl)-abs(centery)<3 and centerxl-centerx<0:
                self.state=Aesquerda
            else:
                if direita<=esquerda and direita<=cima and direita<=baixo:
                    self.state=Adireita    
                elif esquerda<=direita and esquerda<=cima and esquerda<=baixo:
                    self.state=Aesquerda
                elif cima<=direita and cima<=esquerda and cima<=baixo:
                    self.state=Acima
                elif baixo<=direita and baixo<=esquerda and baixo<=cima:
                    self.state=Abaixo
        

        if self.state==Adireita:
            self.speedx=2
            self.speedy=0
        elif self.state==Aesquerda:
            self.speedx=-2
            self.speedy=0
        elif self.state==Acima:
            self.speedx=0
            self.speedy=-2
        elif self.state==Abaixo:
            self.speedx=0
            self.speedy=2

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.left<0 or self.rect.right>COMP:
            self.speedx=-self.speedx
        if self.rect.top<40 or self.rect.bottom>ALTU:
            self.speedy=-self.speedy
        
        
        
        if self.speedx>0:
            self.state=Adireita
            self.hitbox=pygame.Rect(self.rect.x+11,self.rect.y+5,COMP_LINK-47,ALTU_LINK-23)
        elif self.speedx<0:
            self.state=Aesquerda
            self.hitbox=pygame.Rect(self.rect.x+7,self.rect.y+3,COMP_LINK-43,ALTU_LINK-22)
        if self.speedy>0:
            self.state=Abaixo
            self.hitbox=pygame.Rect(self.rect.x+8,self.rect.y+6,COMP_LINK-42,ALTU_LINK-24)
        elif self.speedy<0:
            self.state=Acima
            self.hitbox=pygame.Rect(self.rect.x+7,self.rect.y+4,COMP_LINK-42,ALTU_LINK-25)

       
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
     
class Boss (pygame.sprite.Sprite):
    def __init__ (self,link,sheet):
        pygame.sprite.Sprite.__init__(self)
        self.speedx = 1
        self.speedy = 0

        self.link=link
        
        sheet_i=pygame.transform.scale (sheet,(COMP_LINK*6,ALTU_LINK*9))
        spritesheet = load_spritesheet(sheet_i, 4, 4)

        self.animations = {
            Acima: spritesheet[12:15],
            Abaixo: spritesheet[0:3],
            Adireita: spritesheet[4:7],
            Aesquerda: spritesheet[8:11],
        }

        self.state = Adireita
        self.animation = self.animations[self.state]
        
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect=self.image.get_rect()
        self.rect.x = random.randint (0,COMP-COMP_LINK)
        self.rect.y = random.randint (40,ALTU-ALTU_LINK)

        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 150

        self.hitbox=pygame.Rect(self.rect.x+7,self.rect.y+3,COMP_LINK-34,ALTU_LINK-15)
    def update (self):
        centerxl=self.link.rect.centerx
        centeryl=self.link.rect.centery
        centerx=self.rect.centerx 
        centery=self.rect.centery

        direita=abs(self.rect.right-self.link.rect.left)
        esquerda=abs(self.rect.left-self.link.rect.right)
        cima=abs(self.rect.top-self.link.rect.bottom)
        baixo=abs(self.rect.bottom-self.link.rect.top)

        if abs(centerxl)-abs(centerx)<3 and centeryl-centery>0:
            self.state=Abaixo
        elif abs(centerxl)-abs(centerx)<3 and centeryl-centery<0:
            self.state=Acima
        elif abs(centeryl)-abs(centery)<3 and centerxl-centerx>0:
            self.state=Adireita
        elif abs(centeryl)-abs(centery)<3 and centerxl-centerx<0:
            self.state=Aesquerda
        else:
            if direita<=esquerda and direita<=cima and direita<=baixo:
                self.state=Adireita    
            elif esquerda<=direita and esquerda<=cima and esquerda<=baixo:
                self.state=Aesquerda
            elif cima<=direita and cima<=esquerda and cima<=baixo:
                self.state=Acima
            elif baixo<=direita and baixo<=esquerda and baixo<=cima:
                self.state=Abaixo
        

        if self.state==Adireita:
            self.speedx=1
            self.speedy=0
        elif self.state==Aesquerda:
            self.speedx=-1
            self.speedy=0
        elif self.state==Acima:
            self.speedx=0
            self.speedy=-1
        elif self.state==Abaixo:
            self.speedx=0
            self.speedy=1

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.left<0 or self.rect.right>COMP:
            self.speedx=-self.speedx
        if self.rect.top<40 or self.rect.bottom>ALTU:
            self.speedy=-self.speedy
        
        
        
        if self.state==Adireita:
            self.hitbox=pygame.Rect(self.rect.x+25,self.rect.y+12,COMP_LINK-10,ALTU_LINK+55)
        elif self.state==Aesquerda:
            self.hitbox=pygame.Rect(self.rect.x+25,self.rect.y+12,COMP_LINK-10,ALTU_LINK+45)
        if self.state==Abaixo:
            self.hitbox=pygame.Rect(self.rect.x+25,self.rect.y+12,COMP_LINK-10,ALTU_LINK+55)
        elif self.state==Acima:
            self.hitbox=pygame.Rect(self.rect.x+25,self.rect.y+12,COMP_LINK-10,ALTU_LINK+45)



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

class Lava (pygame.sprite.Sprite):
    def __init__ (self, imagem,pos,link):
        pygame.sprite.Sprite.__init__(self)

        self.spritesheet = load_spritesheet(imagem, 1, 4)
        self.frame = 0
        self.image = self.spritesheet[self.frame]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.hitbox=pygame.Rect (pos[0],pos[1],COMP_LAVA,ALTU_LAVA)
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 200
    def update (self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1
            if self.frame >= len(self.spritesheet):
                self.frame = 0
            center = self.rect.center
            self.image = self.spritesheet[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center
