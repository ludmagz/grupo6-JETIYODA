import pygame

# Função de colisão com os fragmentos de crachá, aumentandos os pontos

def colisao_fragmentos(fragmentos, tela, x, y, fragmentos_cracha, pontos):

    for fragmento in fragmentos[:]:
            fragmento.x -= 5
            tela.blit(fragmentos_cracha, fragmento.topleft)
            if fragmento.colliderect(pygame.Rect(x, y, 104, 124)):
                fragmentos.remove(fragmento)
                pontos += 1
            if fragmento.right < 0:
                fragmentos.remove(fragmento)

    return fragmentos, pontos

# Função de colisão com os "lasers" (tiram vida do jogador)

def colisao_laser(lasers, tela, x, y, foguinho, game_over, vidas):

    for laser in lasers[:]:
            laser.x -= 5
            tela.blit(foguinho, laser.topleft)
            if laser.colliderect(pygame.Rect(x, y, 104, 124)):
                lasers.remove(laser)
                vidas -= 0.5
                if vidas == 0:
                    game_over = True
            if laser.right < 0:
                lasers.remove(laser)
    
    return lasers, game_over, vidas
