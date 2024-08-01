import pygame

# Função de colisão com os fragmentos de crachá, aumentandos os pontos

def colisao_fragmentos(fragmentos, tela, x, y, fragmentos_cracha, pontos, velocidade_objeto):

    for fragmento in fragmentos[:]:
            if fragmento.colliderect(pygame.Rect(x, y, 104, 124)):
                fragmentos.remove(fragmento)
                pontos += 1

    return fragmentos, pontos

# Função de colisão com os "lasers" (tiram vida do jogador)

def colisao_laser(lasers, tela, x, y, foguinho, game_over, vidas, velocidade_objeto, pontos):
    for laser in lasers[:]:
        if laser.colliderect(pygame.Rect(x, y, 104, 124)):
            lasers.remove(laser)
            vidas -= 0.5
            if vidas == 0:
                game_over = True
                pontos = 0
    return lasers, game_over, vidas, pontos

# Função de colisão com os corações (restayram vida do jogaodor)

def colisao_coracao(coracoes, tela, x, y, vida_imagem, vidas, velocidade_objeto):
     
    for coracao in coracoes[:]:
        if coracao.colliderect(pygame.Rect(x, y, 104, 124)):
            coracoes.remove(coracao)
            if vidas < 3:
                vidas += 1
            else:
                vidas = 3
    
    return coracoes, vidas
