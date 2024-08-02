import pygame

# Função de colisão com os fragmentos de crachá, aumentandos os pontos

def colisao_fragmentos(fragmentos, tela, x, y, fragmentos_cracha, pontos, velocidade_objeto,coleta_cracha):

    for fragmento in fragmentos[:]:
            if fragmento.colliderect(pygame.Rect(x, y, 104, 124)):
                fragmentos.remove(fragmento)
                pontos += 1
                coleta_cracha.play()

    return fragmentos, pontos

# Função de colisão com os "lasers" (tiram vida do jogador)

def colisao_laser(lasers, tela, x, y, foguinho, game_over, vidas, velocidade_objeto, infinito,fogo_som):
    
    for laser in lasers[:]:
        if laser.colliderect(pygame.Rect(x, y, 104, 124)):
            lasers.remove(laser)
            if infinito == False:
                vidas -= 0.5
            if vidas == 0:
                game_over = True
            fogo_som.play() 
    return lasers, game_over, vidas

# Função de colisão com os corações (restayram vida do jogaodor)

def colisao_coracao(coracoes, tela, x, y, vida_imagem, vidas, velocidade_objeto,vida_som):
     
    for coracao in coracoes[:]:
        if coracao.colliderect(pygame.Rect(x, y, 104, 124)):
            coracoes.remove(coracao)
            if vidas < 3:
                vidas += 1
            else:
                vidas = 3
            vida_som.play()
    
    return coracoes, vidas

def colisao_robocin(robocins, x, y, infinito, tempo_robocin,robocin_coletado):

    for robo in robocins[:]:
        if robo.colliderect(pygame.Rect(x, y, 104, 124)):
            tempo_robocin = pygame.time.get_ticks()
            infinito = True
            robocins.remove(robo)
            robocin_coletado.play()
    
    return robocins, infinito, tempo_robocin
