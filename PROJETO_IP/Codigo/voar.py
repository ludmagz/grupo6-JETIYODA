import pygame

def voando(y, x, gravidade, altura, sprite_baixo1, sprite_baixo2, sprite_baixo3, sprite_voando, sprite_voando2, tela, espaco, frames, index, pontos, sprite_baixo1_c, sprite_baixo2_c, sprite_baixo3_c, sprite_voando_c, sprite_voando2_c):

    tecla = pygame.key.get_pressed()

    # Se for apertado a tecla espaço, o jogador irá subir (voar)

    if tecla[pygame.K_SPACE]:
        gravidade = 0
        if (y - 20) > 10:
            y -= 5
        else:
            y = 10
    
    # Se não, ele irá cair com uma simulação de gravidade (aceleração)

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

    # Mudança de sprite do personagem de acordo com a ação dele
    if pontos<350:
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
    else:
        if y >= 550:
                if frames % 15 == 0:
                    index = (index + 1) % 3

                if index == 0:
                    tela.blit(sprite_baixo1_c, (x, 550))
                elif index == 1:
                    tela.blit(sprite_baixo2_c, (x, 550))
                elif index == 2:
                    tela.blit(sprite_baixo3_c, (x, 550))

                frames += 1
        elif tecla[pygame.K_SPACE] or espaco:
            tela.blit(sprite_voando_c, (x, y))
            frames = 0
            espaco = False
        else:
            tela.blit(sprite_voando2_c, (x, y))

    return y, x, gravidade, frames, index
