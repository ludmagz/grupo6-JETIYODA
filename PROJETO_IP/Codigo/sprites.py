import pygame
from pygame.locals import *
from obstaculos import *


# Carrega e escala os sprites do personagem andando e voando
def inicializa_sprites():

    sprites = {}

    sprites['baixo1_c'] = pygame.transform.scale(pygame.image.load('sprites/frame2.png').convert_alpha(), (90, 140))
    sprites['baixo2_c'] = pygame.transform.scale(pygame.image.load('sprites/frame1.png').convert_alpha(), (90, 140))
    sprites['baixo3_c'] = pygame.transform.scale(pygame.image.load('sprites/frame3.png').convert_alpha(), (90, 140))
    sprites['voando1_c'] = pygame.transform.scale(pygame.image.load('sprites/frame4.png').convert_alpha(), (90, 140))
    sprites['voando2_c'] = pygame.transform.scale(pygame.image.load('sprites/frame5.png').convert_alpha(), (90, 140))
    
    
    sprites['baixo1'] = pygame.transform.scale(pygame.image.load('sprites/frame8.png').convert_alpha(), (90, 140))
    sprites['baixo2'] = pygame.transform.scale(pygame.image.load('sprites/frame6.png').convert_alpha(), (90, 140))
    sprites['baixo3'] = pygame.transform.scale(pygame.image.load('sprites/frame7.png').convert_alpha(), (90, 140))
    sprites['voando1'] = pygame.transform.scale(pygame.image.load('sprites/frame9.png').convert_alpha(), (90, 140))
    sprites['voando2'] = pygame.transform.scale(pygame.image.load('sprites/frame10.png').convert_alpha(), (90, 140))
    
    return sprites


# Carrega e escala os sprites dos obstáculos e coletáveis
def inicializar_obstaculos():

    obstaculos_sprites = {}

    obstaculos_sprites['foguinho'] = pygame.image.load('coletaveis/foguinho_obstaculo.png').convert_alpha()
    obstaculos_sprites['fragmentos_cracha'] = pygame.image.load('coletaveis/fragmento_cracha.png').convert_alpha()
    obstaculos_sprites['vidas_imagem'] = pygame.image.load('coletaveis/vidas.png').convert_alpha()
    obstaculos_sprites['fragmentos_cracha2'] = pygame.image.load('coletaveis/fragmento_cracha.png').convert_alpha()
    obstaculos_sprites['robocin'] = pygame.image.load('coletaveis/robocin_coletavel.png').convert_alpha()

    return obstaculos_sprites

# Carrega e escala os sprites dos fundos
def inicializar_fundos():

    largura = 1280
    altura = 720
    fundos = ['Fundos/fundo1.png', 'Fundos/fundo2.png', 'Fundos/fundo3.png', 'Fundos/fundo4.png', 'Fundos/fundo5.png']
    backgrounds = []
    for fundo in fundos:
        bg = pygame.transform.scale(pygame.image.load(fundo).convert(), (largura, altura))
        backgrounds.append(bg)
    mapa = 0
    if mapa in range (len(backgrounds)):
        fundo = backgrounds[mapa]
        proximo_fundo = backgrounds[mapa + 1]
    else:
        mapa = 0 
        fundo = backgrounds[mapa]
        proximo_fundo = backgrounds[mapa + 1]
    tela_inicial_fundo = pygame.image.load('tela inicial/telainicial.png').convert()
    tela_inicial_fundo = pygame.transform.scale(tela_inicial_fundo, (largura, altura))
    tela_final1_fundo = pygame.image.load('telas finais/game over 1.png').convert()
    tela_final1_fundo = pygame.transform.scale(tela_final1_fundo, (largura, altura))
    return tela_inicial_fundo, backgrounds, tela_final1_fundo


# Reinicia as variáveis quando preciso
def variaveis(fragmentos, lasers, altura, largura):

    x = 100
    y = (altura / 2) - 40
    velocidade_tela = 1
    gravidade = 0
    pontos = 0
    vidas = 3
    fragmentos = []
    lasers = []
    fragmentos = criar_fragmentos(altura, largura)
    lasers = criar_lasers(altura, largura)

    return x, y, gravidade, pontos, vidas, fragmentos, lasers, velocidade_tela
