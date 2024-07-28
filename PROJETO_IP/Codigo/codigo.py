import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

largura = 1280
altura = 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('JetIyoda TestCase Ride!!')


fonte = pygame.font.SysFont('arial', 40, True, True)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

sprite_baixo1 = pygame.image.load('sprites/frame2.png').convert_alpha()
sprite_baixo2 = pygame.image.load('sprites/frame3.png').convert_alpha()
sprite_baixo3 = pygame.image.load('sprites/frame1.png').convert_alpha()
sprite_baixo1 = pygame.transform.scale(sprite_baixo1, (90, 140))
sprite_baixo2 = pygame.transform.scale(sprite_baixo2, (90, 140))
sprite_baixo3 = pygame.transform.scale(sprite_baixo3, (90, 140))

sprite_voando = pygame.image.load('sprites/frame4.png').convert_alpha()
sprite_voando = pygame.transform.scale(sprite_voando, (90, 140))
sprite_voando2 = pygame.image.load('sprites/frame5.png').convert_alpha()
sprite_voando2 = pygame.transform.scale(sprite_voando2, (90, 140))

fundo = pygame.image.load('Fundos/fundo1.png').convert()
fundo = pygame.transform.scale(fundo, (largura, altura))
tela_inicial_fundo = pygame.image.load('tela inicial/telainicial.png').convert()
tela_inicial_fundo = pygame.transform.scale(tela_inicial_fundo, (largura, altura))


x = 100
y = (altura / 2) - 40
gravidade = 0
espaco = False
game_over = False
pontos = 0
frames = 0
index = 0

fragmentos = []
lasers = []

def criar_fragmentos():
    y_fragmento = random.randint(50, altura - 50)
    for i in range(5):
        x_fragmento = largura + i * 40
        fragmentos.append(pygame.Rect(x_fragmento, y_fragmento, 30, 30))

def criar_lasers():
    y_lasers = random.randint(50, altura - 50)
    for i in range(2):
        x_lasers = largura
        lasers.append(pygame.Rect(x_lasers, y_lasers, 100, 200))

criar_fragmentos()
criar_lasers()

def mostrar_tela_inicial():
    tela.blit(tela_inicial_fundo, (0, 0))
    pygame.display.update()

def game_loop():
    global espaco, game_over, pontos, x, y, gravidade, frames, index
    
    tela_inicial = True
    fps = pygame.time.Clock()
    
    while True:
        fps.tick(100)
        
        if tela_inicial:
            mostrar_tela_inicial()
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_s:
                        tela_inicial = False
                        # Resetar variáveis
                        x = 100
                        y = (altura / 2) - 40
                        gravidade = 0
                        pontos = 0
                        fragmentos.clear()
                        lasers.clear()
                        criar_fragmentos()
                        criar_lasers()
            continue
        
        tela.fill(WHITE)
        texto = f'Pontos: {pontos}'
        texto2 = 'GAME OVER!'
        texto3 = 'aperte "R" para reiniciar'
        texto_formatado = fonte.render(texto, False, RED)
        texto2_formatado = fonte.render(texto2, False, RED)
        texto3_formatado = fonte.render(texto3, False, RED)

        tela.blit(fundo, (0, 0))

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and not game_over:
                    espaco = True
                elif evento.key == pygame.K_r and game_over:
                    game_over = False
                    x = 100
                    y = (altura / 2) - 40
                    gravidade = 0
                    pontos = 0
                    fragmentos.clear()
                    lasers.clear()
                    criar_fragmentos()
                    criar_lasers()

        if game_over:
            tela.blit(texto2_formatado, (480, 250))
            tela.blit(texto3_formatado, (380, 300))
            pygame.display.update()
            continue  

        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_SPACE]:
            gravidade = 0
            if (y - 20) > 10:
                y -= 5
            else:
                y = 10
        else:
            gravidade += 0.3
            if (y + 14) < 550:
                y += gravidade
            else:
                y = 550

        if y < 0:
            y = 0
        elif y > altura - 140:
            y = altura - 140

        if y >= 550:
            if frames % 15 == 0:
                index = (index + 1) % 3

            if index == 0:
                tela.blit(sprite_baixo1, (x, 550))
            elif index == 1:
                tela.blit(sprite_baixo2, (x, 550))
            elif index == 2:
                tela.blit(sprite_baixo3, (x, 550))

            frames += 1
        elif tecla[pygame.K_SPACE] or espaco:
            tela.blit(sprite_voando, (x, y))
            frames = 0
            espaco = False
        else:
            tela.blit(sprite_voando2, (x, y))

        for fragmento in fragmentos[:]:
            fragmento.x -= 5
            pygame.draw.rect(tela, RED, fragmento)
            if fragmento.colliderect(pygame.Rect(x, y, 104, 124)):
                fragmentos.remove(fragmento)
                pontos += 1
            if fragmento.right < 0:
                fragmentos.remove(fragmento)

        for laser in lasers[:]:
            laser.x -= 5
            pygame.draw.rect(tela, (0, 255, 0), laser)
            if laser.colliderect(pygame.Rect(x, y, 104, 124)):
                game_over = True
            if laser.right < 0:
                lasers.remove(laser)

        tela.blit(texto_formatado, (1050, 40))
        pygame.display.update()

        if len(fragmentos) <= 15:
            criar_fragmentos()
        if len(lasers) <= 2:
            criar_lasers()

game_loop()
