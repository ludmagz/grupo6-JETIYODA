# Aqui estão as funções que não precisam de um arquivo destinadas apenas para elas

from obstaculos import *

tamanho_inicial_robocin = [200, 150]
tamanho_inicial_progresso = [720, 270]

def atualizar_tamanho(tamanho, tempo_passado, duracao):

    fator_diminuição = tempo_passado / duracao  # Fator de diminuição por segundo

    tamanho[0] = max(tamanho_inicial_robocin[0] *(1 - fator_diminuição), 0)

def atualizar_tamanho_progresso(tamanho, tempo_passado, duracao):

    fator_diminuição = tempo_passado / duracao  # Fator de diminuição por segundo

    tamanho[0] = max(tamanho_inicial_progresso[0] *(1 - fator_diminuição), 0)

def atualizar_e_desenhar_coletaveis(lista, velocidade_objeto, tela, imagem):
    for unidade in lista[:]:
        unidade.x -= velocidade_objeto
        tela.blit(imagem, unidade.topleft)
        if unidade.right < 0:
            lista.remove(unidade)

# Reinicia as variáveis quando preciso
def variaveis(fragmentos, lasers, altura, largura):

    x = 100
    y = (altura / 2) - 40
    velocidade_tela = 1
    velocidade_objeto = 5
    gravidade = 0
    pontos = 0
    vidas = 3
    fragmentos = []
    lasers = []
    fragmentos = criar_fragmentos(altura, largura)
    lasers = criar_lasers(altura, largura)

    return x, y, gravidade, pontos, vidas, fragmentos, lasers, velocidade_tela, velocidade_objeto
