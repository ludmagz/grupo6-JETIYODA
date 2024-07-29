import pygame
from pygame.locals import *
from obstaculos import *


# Carrega e escala os sprites do personagem andando e voando
def inicializa_sprites():

    sprites = {}

    sprites['baixo1'] = pygame.transform.scale(pygame.image.load('sprites/frame2.png').convert_alpha(), (90, 140))
    sprites['baixo2'] = pygame.transform.scale(pygame.image.load('sprites/frame3.png').convert_alpha(), (90, 140))
    sprites['baixo3'] = pygame.transform.scale(pygame.image.load('sprites/frame1.png').convert_alpha(), (90, 140))
    sprites['voando1'] = pygame.transform.scale(pygame.image.load('sprites/frame4.png').convert_alpha(), (90, 140))
    sprites['voando2'] = pygame.transform.scale(pygame.image.load('sprites/frame5.png').convert_alpha(), (90, 140))
    
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

    fundos = {}

    fundos['fundo1'] = pygame.image.load('Fundos/fundo1.png').convert()
    fundos['tela_inicial_fundo'] = pygame.image.load('tela inicial/telainicial.png').convert()

    return fundos


# Reinicia as variáveis quando preciso
def variaveis(fragmentos, lasers, altura, largura):

    x = 100
    y = (altura / 2) - 40
    gravidade = 0
    pontos = 0
    vidas = 3
    fragmentos = []
    lasers = []
    fragmentos = criar_fragmentos(altura, largura)
    lasers = criar_lasers(altura, largura)

    return x, y, gravidade, pontos, vidas, fragmentos, lasers
