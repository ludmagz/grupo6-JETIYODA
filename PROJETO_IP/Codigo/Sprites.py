# Aqui estão todas as funções que inicializam os sprites (imagens) do jogo, desde os sprites do jogador até os do fundo

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

    sprites['robocin1'] = pygame.transform.scale(pygame.image.load('sprites/robocin1.png').convert_alpha(), (90, 140))
    sprites['robocin2'] = pygame.transform.scale(pygame.image.load('sprites/robocin2.png').convert_alpha(), (90, 140))
    sprites['robocin3'] = pygame.transform.scale(pygame.image.load('sprites/robocin3.png').convert_alpha(), (90, 140))
    sprites['robocin4'] = pygame.transform.scale(pygame.image.load('sprites/robocin4.png').convert_alpha(), (90, 140))
    sprites['robocin5'] = pygame.transform.scale(pygame.image.load('sprites/robocin5.png').convert_alpha(), (90, 140))

    
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
    fundos_ufpe = ['Fundos UFPE/ufpe1.png', 'Fundos UFPE/ufpeCAC.png','Fundos UFPE/ufpeCFCH.png', 'Fundos UFPE/ufpeCTG.png', 'Fundos UFPE/ufpeMATO.png', 'Fundos UFPE/ufpeCIN.png','Fundos UFPE/ufpeMATO2.png']
    backgrounds_ufpe = []
    for fundo in fundos_ufpe:
        bg = pygame.transform.scale(pygame.image.load(fundo).convert(), (largura, altura))
        backgrounds_ufpe.append(bg)
    mapa = 0
    if mapa in range (len(backgrounds_ufpe)):
        fundo = backgrounds_ufpe[mapa]
        proximo_fundo = backgrounds_ufpe[mapa + 1]
    else:
        mapa = 0
        fundo = backgrounds_ufpe[mapa]
        proximo_fundo = backgrounds_ufpe[mapa + 1]
        
    tela_inicial_fundo = pygame.image.load('tela inicial/telainicial.png').convert()
    tela_inicial_fundo = pygame.transform.scale(tela_inicial_fundo, (largura, altura))

    tela_instrucoes_fundo = pygame.image.load('tela inicial/instrucoes.png').convert()
    tela_instrucoes_fundo = pygame.transform.scale(tela_instrucoes_fundo, (largura, altura))

    tela_final1_fundo = pygame.image.load('telas finais/game over 1.png').convert()
    tela_final1_fundo = pygame.transform.scale(tela_final1_fundo, (largura, altura))

    tela_final2_fundo=pygame.image.load('telas finais/game over 2.png').convert()
    tela_final2_fundo = pygame.transform.scale(tela_final2_fundo, (largura, altura))

    tela_final3_fundo=pygame.image.load('telas finais/fundo_chegada.png').convert()
    tela_final3_fundo = pygame.transform.scale(tela_final3_fundo, (largura, altura))

    return tela_inicial_fundo, tela_instrucoes_fundo, backgrounds, tela_final1_fundo, tela_final2_fundo, tela_final3_fundo, backgrounds_ufpe


