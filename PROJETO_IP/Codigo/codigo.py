import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 1280
altura = 960

x = 100
y = (altura / 2) - 40
k = 0
tamanho_linha = 1280
tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('JetIyoda TestCase Ride!!')
fps = pygame.time.Clock()

sprite_baixo1 = pygame.image.load('sprites/frame2.png').convert_alpha()
sprite_baixo2 = pygame.image.load('sprites/frame3.png').convert_alpha()
sprite_baixo3 = pygame.image.load('sprites/frame1.png').convert_alpha()
sprite_baixo1 = pygame.transform.scale(sprite_baixo1, (154, 224))
sprite_baixo2 = pygame.transform.scale(sprite_baixo2, (154, 224))
sprite_baixo3 = pygame.transform.scale(sprite_baixo3, (154, 224))

sprite_voando = pygame.image.load('sprites/frame4.png').convert_alpha()
sprite_voando = pygame.transform.scale(sprite_voando, (154, 224))
sprite_voando2 = pygame.image.load('sprites/frame5.png').convert_alpha()
sprite_voando2 = pygame.transform.scale(sprite_voando2, (154, 224))

voando = False
frames = 0
index = 0


fundo = pygame.image.load('Fundos/fundo1.png').convert()
fundo = pygame.transform.scale(fundo, (largura, altura))
while True:
    fps.tick(100)
    tela.fill((255, 255, 255))

    tela.blit(fundo, (0, 0))

    k -= 50
    tamanho_linha += 30

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_SPACE]:
        if (y - 20) > 10:
            y -= 2.5
        else:
            y = 10
    else:
        if (y + 14) < 720:
            y += 5
        else:
            y = 650

    if y >= 650:
        if frames % 15 == 0:
            index = (index + 1) % 3

        if index == 0:
            tela.blit(sprite_baixo1, (x, 850 - sprite_baixo1.get_height()))
        elif index == 1:
            tela.blit(sprite_baixo2, (x, 850 - sprite_baixo2.get_height()))
        elif index == 2:
            tela.blit(sprite_baixo3, (x, 850 - sprite_baixo3.get_height()))

        frames += 1

    elif pygame.key.get_pressed()[K_SPACE]:
        tela.blit(sprite_voando, (x, y))
        frames = 0 

    else:
        tela.blit(sprite_voando2, (x, y))

    pygame.draw.rect(tela, (0, 255, 0), (1180, 700, k, 100))
    pygame.draw.line(tela, (50, 100, 255), (0, 861), (tamanho_linha, 861))

    pygame.display.update()
