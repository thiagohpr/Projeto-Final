import pygame
from config import FPS, vermelho, COMP, ALTU, verde, preto, verde, QUIT

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

def over_screen (window, score):
    score_font = pygame.font.Font('fonte/PressStart2P.ttf', 28)
    score_font2=pygame.font.Font('fonte/PressStart2P.ttf', 15)

    with open ('recordes.txt','r') as file:
        tudo=file.read()
        lista=tudo.split("---")
    dic={}
    for i in range(len(lista)-1):
        if i==0 or i%2==0:
            dic[lista[i]]=int(lista[i+1])
    
    clock = pygame.time.Clock()
    frames=0
    text=""
    seunome=""
    fim=True
    fim1=True
    fim2=False
    fim3=False
    digitando=False
    digitado=False
    color=preto

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
                    state=QUIT
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
                        state=QUIT
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
                            elif len(text)<=10:
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
                    lista=recordes.split ('---')
            else:
                fim3=True
                fim2=False
            
            pygame.display.update()



        while fim3:     #mostrar o top 5
            clock.tick (FPS)
            window.fill (vermelho)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fim3=False
                    fim=False
                    state=QUIT

            text_surface = score_font.render("{}".format("Melhores Pontuações"), True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.centerx = COMP/2
            text_rect.centery = 90
            window.blit(text_surface, text_rect)



            text_surface = score_font.render("{}".format("1º"), True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.centerx = 100
            text_rect.centery = 175
            window.blit(text_surface, text_rect)

            text_surface = score_font.render("{}".format(lista[0]), True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.x = 150
            text_rect.centery = 175
            window.blit(text_surface, text_rect)

            text_surface = score_font.render("{}".format(lista[1]), True, (255, 255, 0))
            text_rect = text_surface.get_rect()
            text_rect.x = 700
            text_rect.centery = 175
            window.blit(text_surface, text_rect)



            text_surface = score_font.render("{}".format("2º"), True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.centerx = 100
            text_rect.centery = 275
            window.blit(text_surface, text_rect)

            text_surface = score_font.render("{}".format(lista[2]), True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.x = 150
            text_rect.centery = 275
            window.blit(text_surface, text_rect)

            text_surface = score_font.render("{}".format(lista[3]), True, (255, 255, 0))
            text_rect = text_surface.get_rect()
            text_rect.x = 700
            text_rect.centery = 275
            window.blit(text_surface, text_rect)



            text_surface = score_font.render("{}".format("3º"), True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.centerx = 100
            text_rect.centery = 375
            window.blit(text_surface, text_rect)

            text_surface = score_font.render("{}".format(lista[4]), True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.x = 150
            text_rect.centery = 375
            window.blit(text_surface, text_rect)

            text_surface = score_font.render("{}".format(lista[5]), True, (255, 255, 0))
            text_rect = text_surface.get_rect()
            text_rect.x = 700
            text_rect.centery = 375
            window.blit(text_surface, text_rect)



            text_surface = score_font.render("{}".format("4º"), True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.centerx = 100
            text_rect.centery = 475
            window.blit(text_surface, text_rect)

            text_surface = score_font.render("{}".format(lista[6]), True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.x = 150
            text_rect.centery = 475
            window.blit(text_surface, text_rect)

            text_surface = score_font.render("{}".format(lista[7]), True, (255, 255, 0))
            text_rect = text_surface.get_rect()
            text_rect.x = 700
            text_rect.centery = 475
            window.blit(text_surface, text_rect)



            text_surface = score_font.render("{}".format("5º"), True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.centerx = 100
            text_rect.centery = 575
            window.blit(text_surface, text_rect)

            text_surface = score_font.render("{}".format(lista[8]), True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.x = 150
            text_rect.centery = 575
            window.blit(text_surface, text_rect)

            text_surface = score_font.render("{}".format(lista[9]), True, (255, 255, 0))
            text_rect = text_surface.get_rect()
            text_rect.x = 700
            text_rect.centery = 575
            window.blit(text_surface, text_rect)

            pygame.display.update()

    return state