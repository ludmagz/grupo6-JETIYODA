# Aqui estão todas as funções que criam os coletáveis e os obstáculos

import pygame
import random


fragmentos = []
lasers = []
coracoes = []
robocins = []

# Função que cria os fragmentos de crachá (pontos)

def criar_fragmentos(altura, largura):

    y_fragmento = random.randint(50, altura - 50)

    for i in range(5):
        
        x_fragmento = largura + i * 40
        fragmentos.append(pygame.Rect(x_fragmento, y_fragmento, 30, 40))
    
    return fragmentos

# Função que cria os "lasers" (tiram vida do jogador)
def criar_lasers(altura, largura):

    y_lasers = random.randint(50, altura - 50)

    for i in range(2):

        x_lasers = largura
        lasers.append(pygame.Rect(x_lasers, y_lasers, 150, 100))
    
    return lasers

# Função que cria os corações (restauram vida do jogador)
def criar_coracao(altura, largura):

    y_coracao = random.randint(50, altura - 50)

    x = largura

    if len(coracoes) > 0:
        coracoes.clear()
    
    coracoes.append(pygame.Rect(x, y_coracao, 40, 40))

    
    return coracoes

def criar_robocin(altura, largura):

    y = random.randint(50, altura - 50)

    x = largura

    robocins.append(pygame.Rect(x, y, 40, 40))

    return robocins