import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

largura = 1280
altura = 720

fonte = pygame.font.SysFont('arial', 40, True, True)

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
sprite_baixo1 = pygame.transform.scale(sprite_baixo1, (104, 154))
sprite_baixo2 = pygame.transform.scale(sprite_baixo2, (104, 154))
sprite_baixo3 = pygame.transform.scale(sprite_baixo3, (104, 154))

sprite_voando = pygame.image.load('sprites/frame4.png').convert_alpha()
sprite_voando = pygame.transform.scale(sprite_voando, (104, 154))
sprite_voando2 = pygame.image.load('sprites/frame5.png').convert_alpha()
sprite_voando2 = pygame.transform.scale(sprite_voando2, (104, 154))

voando = False
frames = 0
index = 0
pontos = 0

espaco=False

fundo = pygame.image.load('Fundos/fundo1.png').convert()
fundo = pygame.transform.scale(fundo, (largura, altura))

fragmentos = []

def criar_fragmentos():
    y_fragmento = random.randint(50, altura - 50)
    for i in range(5):
        x_fragmento = largura + i * 40
        fragmentos.append(pygame.Rect(x_fragmento, y_fragmento, 30, 30))
criar_fragmentos()

while True:
    fps.tick(100)
    tela.fill((255, 255, 255))
    texto = f'Pontos: {pontos}'
    texto_formatado = fonte.render(texto, False, (255, 0, 0))

    tela.blit(fundo, (0, 0))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()
        elif evento.type==pygame.KEYDOWN:
            if evento.key ==pygame.K_SPACE:
                espaco=True

    if pygame.key.get_pressed()[K_SPACE]:
        if (y - 20) > 10:
            y -= 5
        else:
            y = 10
    else:
        if (y + 14) < 650:
            y += 10
        else:
            y = 420

    if espaco==True:
        if (y - 20) > 10:
            y -= 5
        else:
            y = 10
    else:
        if (y + 14) < 650:
            y += 2.5
        else:
            y = 420

    if y >= 420:
        if frames % 15 == 0:
            index = (index + 1) % 3

        if index == 0:
            tela.blit(sprite_baixo1, (x, 650 - sprite_baixo1.get_height()))
        elif index == 1:
            tela.blit(sprite_baixo2, (x, 650 - sprite_baixo2.get_height()))
        elif index == 2:
            tela.blit(sprite_baixo3, (x, 650 - sprite_baixo3.get_height()))

        frames += 1

    elif pygame.key.get_pressed()[K_SPACE]:
        tela.blit(sprite_voando, (x, y))
        frames = 0
    elif espaco:
            tela.blit(sprite_voando, (x, y))
            frames = 0
            espaco=False
    else:
        tela.blit(sprite_voando2, (x, y))

    for fragmento in fragmentos[:]:
        fragmento.x -= 5
        pygame.draw.rect(tela, (255, 0, 0), fragmento)
        if fragmento.colliderect(pygame.Rect(x, y, 104, 124)):
            fragmentos.remove(fragmento)
            pontos += 1
        if fragmento.right < 0:
            fragmentos.remove(fragmento)

    tela.blit(texto_formatado, (1050, 40))
    pygame.display.update()
    if len(fragmentos) <= 15:
        criar_fragmentos()
