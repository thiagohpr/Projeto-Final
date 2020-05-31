import pygame
import random
import time

pygame.init ()
pygame.font.init ()



Pcima=0
Pbaixo=1
Pdireita=2
Pesquerda=3
Acima=4
Abaixo=5
Adireita=6
Aesquerda=7




COMP=1028
ALTU=708

COMP_LINK=65
ALTU_LINK=60

COMP_LAVA=200
ALTU_LAVA=45

cinza=(46,46,46)
vermelho=(255,0,0)


game=False
inicio=True

window=pygame.display.set_mode((COMP,ALTU))
pygame.display.set_caption ("Jogo Fodinha")
imageml=pygame.image.load ('C:/Users/thpro/Desktop/Desoft/Projeto-Final/lavasprite.png').convert_alpha()
score_font = pygame.font.Font('C:/Users/thpro/Desktop/Desoft/Projeto-Final/PressStart2P.ttf', 28)
score_font2=pygame.font.Font('C:/Users/thpro/Desktop/Desoft/Projeto-Final/PressStart2P.ttf', 15)



with open ('recordes.txt','r') as file:
    tudo=file.read()
    lista=tudo.split("---")
dic={}
for i in range(len(lista)-1):
    if i==0 or i%2==0:
        dic[lista[i]]=int(lista[i+1])

def verificascore (dic, score):
    nome=0
    for n,pont in dic.items():
        if score>pont:
            nome=n
            break
    if nome!=0:
        return nome
    else:
        return False
    

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
        self.hitbox=pygame.Rect(self.rect.x+15,self.rect.y+12,COMP_LINK-35,ALTU_LINK-23)


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

        centerx=self.rect.centerx 
        centery=self.rect.centery
        if (((centerx-centerxl)**2)<20000) and (((centery-centeryl))**2<20000):
                direita=(self.rect.right-self.link.rect.left)**2
                esquerda=(self.rect.left-self.link.rect.right)**2
                cima=(self.rect.top-self.link.rect.bottom)**2
                baixo=(self.rect.bottom-self.link.rect.top)**2
                if direita<esquerda and direita<cima and direita<baixo and self.state==Adireita:
                    self.speedx+=0
                    self.speedy=0
                elif direita<esquerda and direita<cima and direita<baixo and self.state==Aesquerda:
                    self.speedx+=4
                    self.speedy=0
                elif direita<esquerda and direita<cima and direita<baixo and self.state==Acima:
                    self.speedx+=2
                    self.speedy+=2
                elif direita<esquerda and direita<cima and direita<baixo and self.state==Abaixo:
                    self.speedx+=2
                    self.speedy-=2
                
                elif esquerda<direita and esquerda<cima and esquerda<baixo  and self.state==Adireita:
                    self.speedx-=4
                    self.speedy=0
                elif esquerda<direita and esquerda<cima and esquerda<baixo  and self.state==Aesquerda:
                    self.speedx+=0
                    self.speedy=0
                elif esquerda<direita and esquerda<cima and esquerda<baixo  and self.state==Acima:
                    self.speedx-=2
                    self.speedy+=2
                elif esquerda<direita and esquerda<cima and esquerda<baixo  and self.state==Abaixo:
                    self.speedx-=2
                    self.speedy-=2

                elif cima<direita and cima<esquerda and cima<baixo and self.state==Adireita:
                    self.speedx-=2
                    self.speedy-=2
                elif cima<direita and cima<esquerda and cima<baixo and self.state==Aesquerda:
                    self.speedx+=2
                    self.speedy-=2
                elif cima<direita and cima<esquerda and cima<baixo and self.state==Acima:
                    self.speedx=0
                    self.speedy+=0
                elif cima<direita and cima<esquerda and cima<baixo and self.state==Abaixo:
                    self.speedx=0
                    self.speedy-=4
            
                elif baixo<direita and baixo<esquerda and baixo<cima and self.state==Adireita:
                    self.speedx-=2
                    self.speedy+=2
                elif baixo<direita and baixo<esquerda and baixo<cima and self.state==Aesquerda:
                    self.speedx+=2
                    self.speedy+=2
                elif baixo<direita and baixo<esquerda and baixo<cima and self.state==Acima:
                    self.speedx=0
                    self.speedy+=4
                elif baixo<direita and baixo<esquerda and baixo<cima and self.state==Abaixo:
                    self.speedx=0
                    self.speedy+=0

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





def collided(sprite, other):
    return sprite.hitbox.colliderect(other.hitbox)


sheet_m=pygame.image.load ('C:/Users/thpro/Desktop/Desoft/Projeto-Final/sheet_m.png').convert_alpha()
sheet_i=pygame.image.load ('C:/Users/thpro/Desktop/Desoft/Projeto-Final/sheet_i4.png').convert_alpha()
sheet_a=pygame.image.load ('C:/Users/thpro/Desktop/Desoft/Projeto-Final/sheet_a.png').convert_alpha()


all_sprites=pygame.sprite.Group()
all_lava=pygame.sprite.Group()
all_enemies=pygame.sprite.Group()
linkin=pygame.sprite.Group()

posicoes=[[0,200],[500,650],[100,400],[800,500],[500,250],[150,100]]

link=Link(sheet_m)
linki=LinkI(sheet_a)
linkin.add (linki)


for pos in posicoes:
    lava=Lava(imageml,pos,link)
    all_lava.add (lava)
    all_sprites.add (lava)

all_sprites.add (link)


inimigo=Inimigo (link,sheet_i)
all_enemies.add (inimigo)
all_sprites.add (inimigo)


score=1
lives=270
maxini=50


clock = pygame.time.Clock()
FPS=60
frames=0
text=""
seunome=""
digitando=False
digitado=False
preto=(0,0,0)
verde=(0,255,0)
color=preto

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
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                inicio=False
                game=True
    linkin.update()
    linkin.draw (window)
    pygame.display.update()


while game:
    clock.tick (FPS)

 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
                
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                link.speedx -= 3
                
            if event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                link.speedx += 3
                
            if event.key == pygame.K_UP or event.key==pygame.K_w:
                link.speedy -= 3
                
            if event.key == pygame.K_DOWN or event.key==pygame.K_s:
                link.speedy += 3
                
       
        if event.type == pygame.KEYUP:
           
            if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                link.speedx += 3
                link.state=Pesquerda
            if event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                link.speedx -= 3
                link.state=Pdireita
            if event.key == pygame.K_UP or event.key==pygame.K_w:
                link.speedy += 3
                link.state=Pcima
            if event.key == pygame.K_DOWN or event.key==pygame.K_s:
                link.speedy -= 3
                link.state=Pbaixo
    
    if score%500==0 and len (all_enemies)<=maxini:
        inimigo=Inimigo (link,sheet_i)
        all_enemies.add (inimigo)
        all_sprites.add (inimigo)


    hitsi=pygame.sprite.spritecollide(link, all_enemies, True, collided)
    hitsl=pygame.sprite.spritecollide(link, all_lava, False, collided)
    if len (hitsi)>0:
        lives-=75
    if len (hitsl)>0:
        lives-=2
        

    if lives<=0:
        lives=0
        game=False
        fim=True
        fim1=True


    score+=1
    window.fill(cinza)
   

    vertices=[(COMP-(COMP-4),ALTU-(ALTU-5)),(COMP-4,ALTU-(ALTU-5)),(COMP-4,ALTU-(ALTU-40)),(COMP-(COMP-4),ALTU-(ALTU-40))]
    pygame.draw.polygon (window, (0,0,0), vertices)
    vertices2=(4,5,1020,35)
    pygame.draw.rect (window,(0,255,0),vertices2,3)

    # pygame.draw.rect (window,(255,0,0),link.hitbox,2)
    # for inimigo in all_enemies:
    #     pygame.draw.rect (window,(255,0,0),inimigo.hitbox,2)
    
    


    text_surface = score_font.render("{:08d}".format(score), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (COMP / 2,  10)
    window.blit(text_surface, text_rect)

    text_surface = score_font.render(chr(9829), True, (255, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = (13,40)
    window.blit(text_surface, text_rect)


    vida=[(55,14),(lives+55,14),(lives+55,30),(55,30)]
    pygame.draw.polygon (window,vermelho,vida)
    
    vertices3=(55,14,270,16)
    pygame.draw.rect (window,vermelho,vertices3,3)

 

    all_sprites.update()
    all_sprites.draw(window)
    pygame.display.update()

while fim:
    while fim1:
        clock.tick (FPS)
        window.fill (vermelho)
        text_surface = score_font.render("{}".format("Você morreu!"), True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.centerx = COMP/2
        text_rect.centery = ALTU/2
        window.blit(text_surface, text_rect)
        frames+=1
        if frames>240:
            fim1=False
            fim2=True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim1=False
                fim=False
        pygame.display.update()

    while fim2:
        clock.tick (FPS)
        window.fill (vermelho)
        nome=verificascore (dic,score)
        


        if nome!=False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fim2=False
                    fim=False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        digitando=True
                        color=verde
                if event.type == pygame.KEYDOWN:
                    if digitando==True:
                        if event.key == pygame.K_BACKSPACE and text!="":
                            text = text[:-1]
                        elif event.key == pygame.K_RETURN and text!="":
                            seunome=text
                            digitado=True
                        else:
                            text += event.unicode

            input_box = pygame.Rect(364, 319, 300, 70)

            text_surface = score_font.render("{}".format("Você está entre os 5 melhores!"), True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.centerx = COMP/2
            text_rect.centery = 90
            window.blit(text_surface, text_rect)

            text_surface = score_font2.render("{}".format("Digite o seu nome:"), True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.centerx = COMP/2
            text_rect.centery = 300
            window.blit(text_surface, text_rect)

            text_surface = score_font.render("{}".format(score), True, (255, 255, 0))
            text_rect = text_surface.get_rect()
            text_rect.centerx = COMP/2
            text_rect.centery = 150
            window.blit(text_surface, text_rect)


            pygame.draw.rect(window,color, input_box, 4)
            text_surface = score_font2.render("{}".format(text), True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.centerx = COMP/2
            text_rect.centery = ALTU/2
            window.blit(text_surface, text_rect)

            if digitado==True:
                fim2=False
                fim3=True
                novodic={}
                dic2={}
 
                for n,s in dic.items():
                    if nome!=n:
                        novodic[n]=s
                    else:
                        novodic[seunome]=score
                        novodic[n]=s

                i=0
                for n,s in novodic.items():
                    if i!=5:
                        dic2[n]=s
                        i+=1

                recordes=""
                i=0
                for n,s in dic2.items():
                    recordes+=n
                    recordes+="---"
                    recordes+=str(s)
                    i+=1
                    if i!=5:
                        recordes+="---"

                with open ('recordes.txt','w+') as file:
                    file.write (recordes)
        else:
            fim3=True
        
        pygame.display.update()



    while fim3:     #mostrar o top 5
        clock.tick (FPS)
        window.fill (vermelho)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim3=False
                fim=False
        pygame.display.update()

    


pygame.quit()