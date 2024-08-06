# Aqui estão as funções para criar os coletáveis/ obstáculos de forma que eles não ocupem a mesma coordenada


import pygame
import random


def atualizar_intervalos(fragmentos, lasers, existe_robocin, robocins, largura):
    listinha_de_intervalos = []

    if fragmentos:
        ultimo_frag = fragmentos[-1].bottomright
        if ultimo_frag[0] > largura - 30:
            for i in range(ultimo_frag[1] - 43 - 100, ultimo_frag[1] + 3):
                listinha_de_intervalos.append(i)

    if len(fragmentos) > 5:
        ultimo_frag2 = fragmentos[-6].bottomright
        if ultimo_frag2[0] > largura - 30:
            for i in range(ultimo_frag2[1] - 43 - 100, ultimo_frag2[1] + 3):
                listinha_de_intervalos.append(i)

    if len(fragmentos) > 10:
        ultimo_frag3 = fragmentos[-11].bottomright
        if ultimo_frag3[0] > largura - 30:
            for i in range(ultimo_frag3[1] - 43 - 100, ultimo_frag3[1] + 3):
                listinha_de_intervalos.append(i)

    if lasers:
        ultimo_laser = lasers[-1].bottomright
        if ultimo_laser[0] > largura - 10:
            for i in range(ultimo_laser[1] - 103 - 100, ultimo_laser[1] + 3):
                listinha_de_intervalos.append(i)

    if len(lasers) > 1:
        penultimo_laser = lasers[-2].bottomright
        if penultimo_laser[0] > largura - 10:
            for i in range(penultimo_laser[1] - 103 - 100, penultimo_laser[1] + 3):
                listinha_de_intervalos.append(i)

    if existe_robocin and robocins:
        ultimo_robocin = robocins[0].bottomright
        if ultimo_robocin[0] > largura - 10:
            for i in range(ultimo_robocin[1] - 43 - 100, ultimo_robocin[1] + 3):
                listinha_de_intervalos.append(i)

    return listinha_de_intervalos

def atualizar_intervalos_e_adicionar_robocin(fragmentos, lasers, existe_coracao, coracoes, largura, altura, robocins):
    listinha_de_intervalos = []

    def adicionar_intervalos(ultimo_frag, offset_x, offset_y):
        if ultimo_frag[0] > largura - offset_x:
            for i in range(ultimo_frag[1] - offset_y - 100, ultimo_frag[1] + 3):
                listinha_de_intervalos.append(i)

    if fragmentos:
        adicionar_intervalos(fragmentos[-1].bottomright, 30, 43)
    if len(fragmentos) > 5:
        adicionar_intervalos(fragmentos[-6].bottomright, 30, 43)
    if len(fragmentos) > 10:
        adicionar_intervalos(fragmentos[-11].bottomright, 30, 43)
    if lasers:
        adicionar_intervalos(lasers[-1].bottomright, 10, 103)
    if len(lasers) > 1:
        adicionar_intervalos(lasers[-2].bottomright, 10, 103)
    if existe_coracao and coracoes:
        adicionar_intervalos(coracoes[0].bottomright, 10, 43)

    y_robocin = random.randint(50, altura - 50)
    x_robocin = largura

    while y_robocin in listinha_de_intervalos:
        y_robocin = random.randint(50, altura - 50)

    robocins.append(pygame.Rect(x_robocin, y_robocin, 40, 40))

    return listinha_de_intervalos, robocins

def atualizar_intervalos_e_adicionar_fragmentos(fragmentos, lasers, existe_coracao, coracoes, existe_robocin, robocins, largura, altura):
    listinha_de_intervalos = []

    def adicionar_intervalos(ultimo_item, offset_x, offset_y):
        if ultimo_item[0] > largura - offset_x:
            for i in range(ultimo_item[1] - offset_y - 100, ultimo_item[1] + 3):
                listinha_de_intervalos.append(i)

    if fragmentos:
        adicionar_intervalos(fragmentos[-1].bottomright, 30, 43)
    if len(fragmentos) > 5:
        adicionar_intervalos(fragmentos[-6].bottomright, 30, 43)
    if len(fragmentos) > 10:
        adicionar_intervalos(fragmentos[-11].bottomright, 30, 43)
    if lasers:
        adicionar_intervalos(lasers[-1].bottomright, 10, 103)
    if len(lasers) > 1:
        adicionar_intervalos(lasers[-2].bottomright, 10, 103)
    if existe_coracao and coracoes:
        adicionar_intervalos(coracoes[0].bottomright, 10, 43)
    if existe_robocin and robocins:
        adicionar_intervalos(robocins[0].bottomright, 10, 43)

    y_fragmento = random.randint(50, altura - 50)

    while y_fragmento in listinha_de_intervalos:
        y_fragmento = random.randint(50, altura - 50)

    for i in range(5):
        x_fragmento = largura + i * 40
        fragmentos.append(pygame.Rect(x_fragmento, y_fragmento, 30, 40))

    return listinha_de_intervalos, fragmentos

def atualizar_intervalos_e_adicionar_lasers(fragmentos, lasers, existe_coracao, coracoes, existe_robocin, robocins, largura, altura):
    listinha_de_intervalos = []

    def adicionar_intervalos(ultimo_item, offset_x, offset_y):
        if ultimo_item[0] > largura - offset_x:
            for i in range(ultimo_item[1] - offset_y - 100, ultimo_item[1] + 3):
                listinha_de_intervalos.append(i)

    if fragmentos:
        adicionar_intervalos(fragmentos[-1].bottomright, 30, 43)
    if len(fragmentos) > 5:
        adicionar_intervalos(fragmentos[-6].bottomright, 30, 43)
    if len(fragmentos) > 10:
        adicionar_intervalos(fragmentos[-11].bottomright, 30, 43)
    if lasers:
        adicionar_intervalos(lasers[-1].bottomright, 10, 103)
    if len(lasers) > 1:
        adicionar_intervalos(lasers[-2].bottomright, 10, 103)
    if existe_coracao and coracoes:
        adicionar_intervalos(coracoes[0].bottomright, 10, 43)
    if existe_robocin and robocins:
        adicionar_intervalos(robocins[0].bottomright, 10, 43)

    y_lasers = random.randint(50, altura - 50)
    while y_lasers in listinha_de_intervalos:
        y_lasers = random.randint(50, altura - 50)

    for i in range(2):
        x_lasers = largura
        lasers.append(pygame.Rect(x_lasers, y_lasers, 150, 100))

    return listinha_de_intervalos, lasers

def atualizar_intervalos_e_adicionar_coracao(fragmentos, lasers, existe_robocin, robocins, coracoes, largura, altura):
    listinha_de_intervalos = []

    def adicionar_intervalos(ultimo_item, offset_x, offset_y):
        if ultimo_item[0] > largura - offset_x:
            for i in range(ultimo_item[1] - offset_y - 100, ultimo_item[1] + 3):
                listinha_de_intervalos.append(i)

    if fragmentos:
        adicionar_intervalos(fragmentos[-1].bottomright, 30, 43)
    if len(fragmentos) > 5:
        adicionar_intervalos(fragmentos[-6].bottomright, 30, 43)
    if len(fragmentos) > 10:
        adicionar_intervalos(fragmentos[-11].bottomright, 30, 43)
    if lasers:
        adicionar_intervalos(lasers[-1].bottomright, 10, 103)
    if len(lasers) > 1:
        adicionar_intervalos(lasers[-2].bottomright, 10, 103)
    if existe_robocin and robocins:
        adicionar_intervalos(robocins[0].bottomright, 10, 43)

    existe_coracao = True
    tempo = pygame.time.get_ticks()

    y_coracao = random.randint(50, altura - 50)
    x_coracao = largura

    while y_coracao in listinha_de_intervalos:
        y_coracao = random.randint(50, altura - 50)

    if coracoes:
        coracoes.clear()
    
    coracoes.append(pygame.Rect(x_coracao, y_coracao, 40, 40))

    return listinha_de_intervalos, existe_coracao, tempo, coracoes