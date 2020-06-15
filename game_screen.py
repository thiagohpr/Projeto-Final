import pygame
from config import FPS, iniciais, posicoes, COMP, vermelho, azul, podermax, maxini, branco, ALTU, cinza, FIM, QUIT, Pcima, Pbaixo, Pesquerda, Pdireita 
from classes import Link, Flecha, Inimigo, Boss, Lava


def collided(sprite, other):
    return sprite.hitbox.colliderect(other.hitbox)

def game_screen (window):
    game=True
    ataque=False
    chefao=False
    clock = pygame.time.Clock()

    vidab=5
    
    score_font = pygame.font.Font('fonte/PressStart2P.ttf', 28)
    
    sheet_m=pygame.image.load ('img/sheet_m.png').convert_alpha()
    sheet_i=pygame.image.load ('img/sheet_i4.png').convert_alpha()
    imageml=pygame.image.load ('img/lavasprite.png').convert_alpha()

    flechad=pygame.image.load ('img/flechad.png').convert_alpha()
    flechae=pygame.image.load ('img/flechae.png').convert_alpha()
    flechac=pygame.image.load ('img/flechac.png').convert_alpha()
    flechab=pygame.image.load ('img/flechab.png').convert_alpha()
    flechas=[flechad,flechae,flechac,flechab]

    somi=pygame.mixer.Sound('som/inimigo.wav')
    somf=pygame.mixer.Sound('som/flecha.wav')
    dano=pygame.mixer.Sound('som/dano.wav')

    all_sprites=pygame.sprite.Group()
    all_lava=pygame.sprite.Group()
    all_enemies=pygame.sprite.Group()
    all_flechas=pygame.sprite.Group()
    all_boss=pygame.sprite.Group()

    link=Link(sheet_m)

    for pos in posicoes:
        lava=Lava(imageml,pos,link)
        all_lava.add (lava)
        all_sprites.add (lava)

    all_sprites.add (link)
    for i in range (iniciais):
        inimigo=Inimigo (link,sheet_i)
        all_enemies.add (inimigo)
        all_sprites.add (inimigo)
    score=1
    lives=270
    poder=0
    ppoder=0
    while game:
        clock.tick (FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game=False
                state=QUIT
                    
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                    link.speedx -= 3
                    
                if event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                    link.speedx += 3
                    
                if event.key == pygame.K_UP or event.key==pygame.K_w:
                    link.speedy -= 3
                    
                if event.key == pygame.K_DOWN or event.key==pygame.K_s:
                    link.speedy += 3
                if event.key == pygame.K_SPACE and ppoder>90:
                    somf.play()
                    ataque=True
                    flecha=Flecha(link,flechas)
                    all_flechas.add (flecha)
                    all_sprites.add (flecha)
        
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
        if score%5000==0:
            boss=Boss(link,sheet_i)
            all_boss.add (boss)
            all_sprites.add (boss)
            chefao=True
            e=0
            for ini in all_enemies:
                if e<=3:
                    ini.kill()
                    e+=1
            

        hitsi=pygame.sprite.spritecollide(link, all_enemies, True, collided)
        hitsl=pygame.sprite.spritecollide(link, all_lava, False, collided)
        hitsf=pygame.sprite.groupcollide (all_flechas,all_enemies, True,True)
        hitsb=pygame.sprite.spritecollide(link,all_boss,True,collided)
        hitsfb=pygame.sprite.groupcollide (all_flechas,all_boss, True,False)
        if len (hitsi)>0:
            lives-=75
            dano.play()
        if len (hitsl)>0:
            lives-=2
            dano.play()
        if len (hitsf)>0:
            score+=500
            inimigo=Inimigo (link,sheet_i)
            all_enemies.add (inimigo)
            all_sprites.add (inimigo)
            somi.play()
        if len (hitsb)>0:
            dano.play()
            game=False
            state=FIM     
        if len (hitsfb)>0:
            vidab-=1
            somi.play()
            if vidab==0:
                for boss in all_boss:
                    boss.kill()
                chefao=False
                score+=1000
                vidab=5
                
        if lives<=0:
            lives=0
            game=False
            state=FIM

        score+=1
        poder+=link.poder

        if poder%2==0 and poder!=0:
            ppoder+=1
            poder=0
        
        if ppoder>=podermax:
            ppoder=podermax-1

        if ataque==True:
            ppoder-=90
            ataque=False

        
        window.fill(cinza)
    

        vertices=[(COMP-(COMP-4),ALTU-(ALTU-5)),(COMP-4,ALTU-(ALTU-5)),(COMP-4,ALTU-(ALTU-40)),(COMP-(COMP-4),ALTU-(ALTU-40))]
        pygame.draw.polygon (window, (0,0,0), vertices)
        vertices2=(4,5,1020,35)
        pygame.draw.rect (window,(0,255,0),vertices2,3)


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



        bpoder=[(700,14),(ppoder+700,14),(ppoder+700,30),(700,30)]
        pygame.draw.polygon (window,azul,bpoder)

        vertices3=(700,14,podermax,16)
        pygame.draw.rect (window,branco,vertices3,3)
        barra1=[(790,14),(791,14),(791,30),(790,30)]
        pygame.draw.polygon (window,branco,barra1)
        barra2=[(880,14),(881,14),(881,30),(880,30)]
        pygame.draw.polygon (window,branco,barra2)

        if chefao==True:
            bboss=[(364,50),(60*vidab+364,50),(60*vidab+364,70),(364,70)]
            pygame.draw.polygon (window,vermelho,bboss)
            bvert=(364,50,300,20)
            pygame.draw.rect (window, vermelho,bvert,3)


        all_sprites.update()
        all_sprites.draw(window)
        pygame.display.update()
    return state, score