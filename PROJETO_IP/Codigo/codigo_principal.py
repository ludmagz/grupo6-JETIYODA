import pygame
from pygame.locals import *
from sys import exit
from time import *
from sprites import *
from voar import *
from obstaculos import *
from colisoes import *

pygame.init()

largura = 1280
altura = 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('JetIyoda TestCase Ride!!')

fonte = pygame.font.SysFont('arial', 40, True, True)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Chamada das funções de inicialização das imagens ===========

sprites = inicializa_sprites()

tela_inicial_fundo, backgrounds, tela_final1_fundo = inicializar_fundos()

obstaculos_sprites = inicializar_obstaculos()


# Declaração + formatação de cada sprite

sprite_baixo1 = sprites['baixo1']
sprite_baixo2 = sprites['baixo2']
sprite_baixo3 = sprites['baixo3']
sprite_voando = sprites['voando1']
sprite_voando2 = sprites['voando2']

sprite_baixo1 = pygame.transform.scale(sprite_baixo1, (90, 140))
sprite_baixo2 = pygame.transform.scale(sprite_baixo2, (90, 140))
sprite_baixo3 = pygame.transform.scale(sprite_baixo3, (90, 140))

sprite_voando = pygame.transform.scale(sprite_voando, (90, 140))
sprite_voando2 = pygame.transform.scale(sprite_voando2, (90, 140))

sprite_baixo1_c = sprites['baixo1_c']
sprite_baixo2_c = sprites['baixo2_c']
sprite_baixo3_c = sprites['baixo3_c']
sprite_voando_c = sprites['voando1_c']
sprite_voando2_c = sprites['voando2_c']

sprite_baixo1_c = pygame.transform.scale(sprite_baixo1_c, (90, 140))
sprite_baixo2_c = pygame.transform.scale(sprite_baixo2_c, (90, 140))
sprite_baixo3_c = pygame.transform.scale(sprite_baixo3_c, (90, 140))

sprite_voando_c = pygame.transform.scale(sprite_voando_c, (90, 140))
sprite_voando2_c = pygame.transform.scale(sprite_voando2_c, (90, 140))


fragmentos_cracha = obstaculos_sprites['fragmentos_cracha']
foguinho = obstaculos_sprites['foguinho']
fragmentos_cracha2 = obstaculos_sprites['fragmentos_cracha2']
vidas_imagem = obstaculos_sprites['vidas_imagem']
robocin = obstaculos_sprites['robocin']

fragmentos_cracha = pygame.transform.scale(fragmentos_cracha, (30, 40))
foguinho = pygame.transform.scale(foguinho, (150, 100))
fragmentos_cracha2 = pygame.transform.scale(fragmentos_cracha, (30, 40))
vidas_imagem = pygame.transform.scale(vidas_imagem,(40,40))
robocin = pygame.transform.scale(robocin,(30,30))


# Variáveis iniciais =========================================

x = 100
y = (altura / 2) - 40
velocidade_tela = 1
velocidade_objeto = 5
gravidade = 0
espaco = False
game_over = False
pontos = 0
vidas = 3
frames = 0
index = 0
existe_coracao = False
tempo = pygame.time.get_ticks()
posicao_mapa = 0
mapa = 0
fundo = backgrounds[mapa]
proximo_fundo = backgrounds[(mapa + 1)]

# Inicialização dos obstáculos ================================

fragmentos = criar_fragmentos(altura, largura)
lasers = criar_lasers(altura, largura)
coracao = criar_coracao(altura, largura)

def mostrar_tela_inicial():
    tela.blit(tela_inicial_fundo, (0, 0))
    pygame.display.update()


# Loop principal do jogo ======================================

def game_loop():
    global espaco, game_over, pontos, x, y, gravidade, frames, index, vidas, existe_coracao, tempo, posicao_mapa, mapa, fundo, proximo_fundo, velocidade_tela, velocidade_objeto
    
    tela_inicial = True
    fps = pygame.time.Clock()
    
    while True:
        fps.tick(100)
        
        if tela_inicial:
            mostrar_tela_inicial()
            for evento in pygame.event.get():

                # Sair do jogo ainda na tela inicial
                if evento.type == QUIT:
                    pygame.quit()
                    exit()

                # Sair da tela inicial
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_s:
                        tela_inicial = False

                        fragmentos = []
                        lasers = []
                        x, y, gravidade, pontos, vidas, fragmentos, lasers, velocidade_tela, velocidade_objeto = variaveis(fragmentos, lasers, altura, largura)
            continue
        
        # Inicialização/ formatação dos textos que aparecem

        tela.fill(WHITE)
        texto = f': {pontos}'
        texto1=f': {int(vidas)}'

        # Carregamento e progressão do mapa

        if not game_over:
            posicao_mapa -= velocidade_tela

            if pygame.time.get_ticks() % 10000:
                velocidade_tela += 0.001
                velocidade_objeto += 0.002

            if posicao_mapa <= -largura:
                posicao_mapa = 0
                if mapa + 1 in range(len(backgrounds)):
                    mapa += 1
                    fundo = backgrounds[mapa]
                    if mapa + 1 in range(len(backgrounds)):
                        proximo_fundo = backgrounds[(mapa + 1)]
                    else:
                        mapa = 0
                        proximo_fundo = backgrounds[(mapa + 1)]
                    
        
        tela.blit(fundo, (posicao_mapa, 0))
        tela.blit(proximo_fundo, (posicao_mapa + largura, 0))

        texto_formatado = fonte.render(texto, False, RED)
        texto1_formatado=fonte.render(texto1, False, RED)

        for evento in pygame.event.get():

            # Sair do jogo fora da tela inicial
            if evento.type == QUIT:
                pygame.quit()
                exit()

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and not game_over:
                    espaco = True
                elif evento.key == pygame.K_r and game_over:
                    game_over = False
                    x, y, gravidade, pontos, vidas, fragmentos, lasers, velocidade_tela, velocidade_objeto = variaveis(fragmentos, lasers, altura, largura)
        
        # Tela de Game Over
        if game_over:
            tela.blit(tela_final1_fundo, (0, 0))
            pygame.display.flip()
            continue  
        
        # Função para voar
        y, x, gravidade, frames, index = voando(y, x, gravidade, altura, sprite_baixo1, sprite_baixo2, sprite_baixo3, sprite_voando, sprite_voando2, tela, espaco, frames, index, pontos, sprite_baixo1_c, sprite_baixo2_c, sprite_baixo3_c, sprite_voando_c, sprite_voando2_c)

        # Funções de colisões com os fragmentos de crachá e "lasers"
        fragmentos, pontos = colisao_fragmentos(fragmentos, tela, x, y, fragmentos_cracha, pontos, velocidade_objeto)
        lasers, game_over, vidas = colisao_laser(lasers, tela, x, y, foguinho, game_over, vidas, velocidade_objeto)
        
        if existe_coracao == True:
            coracoes, vidas = colisao_coracao(coracoes, tela, x, y, vidas_imagem, vidas, velocidade_objeto)
        
        tela.blit(fragmentos_cracha2, (1050, 40))
        tela.blit(texto_formatado, (1090, 40))
        tela.blit(vidas_imagem,(30,45))
        tela.blit(texto1_formatado, (80, 40))

        pygame.display.flip()

        if len(fragmentos) <= 15:
            fragmentos = criar_fragmentos(altura, largura)
        if len(lasers) <= 2:
            lasers = criar_lasers(altura, largura)

        agora = pygame.time.get_ticks()

        if (agora - tempo) >= 5000:
            existe_coracao = True
            tempo = pygame.time.get_ticks()
            coracoes = criar_coracao(altura, largura)
        
game_loop()
