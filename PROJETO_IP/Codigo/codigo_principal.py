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

fundos = inicializar_fundos()

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

fundo1 = fundos['fundo1']
tela_inicial_fundo = fundos['tela_inicial_fundo']

fundo1 = pygame.transform.scale(fundo1, (largura, altura))
tela_inicial_fundo = pygame.transform.scale(tela_inicial_fundo, (largura, altura))

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
gravidade = 0
espaco = False
game_over = False
pontos = 0
vidas = 3
frames = 0
index = 0
existe_coracao = False
tempo = pygame.time.get_ticks()

# Inicialização dos obstáculos ================================

fragmentos = criar_fragmentos(altura, largura)
lasers = criar_lasers(altura, largura)
coracao = criar_coracao(altura, largura)

def mostrar_tela_inicial():
    tela.blit(tela_inicial_fundo, (0, 0))
    pygame.display.update()


# Loop principal do jogo ======================================

def game_loop():
    global espaco, game_over, pontos, x, y, gravidade, frames, index, vidas, existe_coracao, tempo
    
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
                        x, y, gravidade, pontos, vidas, fragmentos, lasers = variaveis(fragmentos, lasers, altura, largura)
            continue
        
        # Inicialização/ formatação dos textos que aparecem

        tela.fill(WHITE)
        texto = f': {pontos}'
        texto2 = 'GAME OVER!'
        texto3 = 'aperte "R" para reiniciar'
        texto4=f': {int(vidas)}'

        texto_formatado = fonte.render(texto, False, RED)
        texto2_formatado = fonte.render(texto2, False, RED)
        texto3_formatado = fonte.render(texto3, False, RED)
        texto4_formatado=fonte.render(texto4, False, RED)

        tela.blit(fundo1, (0, 0))

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
                    x, y, gravidade, pontos, vidas, fragmentos, lasers = variaveis(fragmentos, lasers, altura, largura)
        
        # Tela de Game Over
        if game_over:
            tela.blit(texto2_formatado, (480, 250))
            tela.blit(texto3_formatado, (380, 300))
            pygame.display.update()
            continue  
        
        # Função para voar
        y, x, gravidade, frames, index = voando(y, x, gravidade, altura, sprite_baixo1, sprite_baixo2, sprite_baixo3, sprite_voando, sprite_voando2, tela, espaco, frames, index)

        # Funções de colisões com os fragmentos de crachá e "lasers"
        fragmentos, pontos = colisao_fragmentos(fragmentos, tela, x, y, fragmentos_cracha, pontos)
        lasers, game_over, vidas = colisao_laser(lasers, tela, x, y, foguinho, game_over, vidas)
        
        if existe_coracao == True:
            coracoes, vidas = colisao_coracao(coracoes, tela, x, y, vidas_imagem, vidas)
        


        tela.blit(fragmentos_cracha2, (1050, 40))
        tela.blit(texto_formatado, (1090, 40))
        tela.blit(vidas_imagem,(30,45))
        tela.blit(texto4_formatado, (80, 40))
        pygame.display.update()

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
