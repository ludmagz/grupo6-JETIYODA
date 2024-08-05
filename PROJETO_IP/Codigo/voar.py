import pygame

def voando(y, x, gravidade, altura):

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

    return y, x, gravidade

def mudanca_sprites(index, frames, infinito, tela, x, y, pontos, sprite_baixo1, sprite_baixo2, sprite_baixo3, sprite_robocin1, sprite_robocin2, sprite_robocin3, sprite_voando, sprite_robocin4, sprite_voando2, sprite_robocin5, sprite_baixo1_c, sprite_baixo2_c, sprite_baixo3_c, sprite_voando_c, sprite_voando2_c):

    tecla = pygame.key.get_pressed()
    # Mudança de sprite do personagem de acordo com a ação dele
    if pontos<350:

        if y >= 550:
                
                if frames % 15 == 0:
                    index = (index + 1) % 3

                if index == 0 and infinito == False:
                    tela.blit(sprite_baixo1, (x, 550))
                elif index == 1 and infinito == False:
                    tela.blit(sprite_baixo2, (x, 550))
                elif index == 2 and infinito == False:
                    tela.blit(sprite_baixo3, (x, 550))
                
                elif index == 0 and infinito == True:
                    tela.blit(sprite_robocin1, (x, 550))
                elif index == 1 and infinito == True:
                    tela.blit(sprite_robocin2, (x, 550))
                elif index == 2 and infinito == True:
                    tela.blit(sprite_robocin3, (x, 550))


                frames += 1

        elif tecla[pygame.K_SPACE] and infinito == False:
            tela.blit(sprite_voando, (x, y))
            frames = 0

        
        elif tecla[pygame.K_SPACE] and infinito == True:
            tela.blit(sprite_robocin4, (x, y))
            frames = 0


        else:
            if infinito == False:
                tela.blit(sprite_voando2, (x, y))
        
            else:
                tela.blit(sprite_robocin5, (x, y))
    else:
        if y >= 550:
                if frames % 15 == 0:
                    index = (index + 1) % 3

                if index == 0 and infinito == False:
                    tela.blit(sprite_baixo1_c, (x, 550))
                elif index == 1 and infinito == False:
                    tela.blit(sprite_baixo2_c, (x, 550))
                elif index == 2 and infinito == False:
                    tela.blit(sprite_baixo3_c, (x, 550))

                elif index == 0 and infinito == True:
                    tela.blit(sprite_robocin1, (x, 550))
                elif index == 1 and infinito == True:
                    tela.blit(sprite_robocin2, (x, 550))
                elif index == 2 and infinito == True:
                    tela.blit(sprite_robocin3, (x, 550))

                frames += 1

        elif tecla[pygame.K_SPACE] and infinito == False:

            tela.blit(sprite_voando_c, (x, y))
            frames = 0

        elif tecla[pygame.K_SPACE] and infinito == True:
            tela.blit(sprite_robocin4, (x, y))
            frames = 0

        else:
            if infinito == False:
                tela.blit(sprite_voando2_c, (x, y))
            else:
                tela.blit(sprite_robocin5, (x, y))

    return y, x, frames, index