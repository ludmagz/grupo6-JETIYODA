import pygame
from pygame.locals import *
from sys import exit
from time import *
from Sprites import *
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

tela_inicial_fundo, tela_instrucoes_fundo, backgrounds, tela_final1_fundo, tela_final2_fundo,tela_final3_fundo = inicializar_fundos()

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

sprites_robocin1 = sprites['robocin1']
sprites_robocin2 = sprites['robocin2']
sprites_robocin3 = sprites['robocin3']
sprites_robocin4 = sprites['robocin4']
sprites_robocin5 = sprites['robocin5']

sprites_robocin1 = pygame.transform.scale(sprites_robocin1, (100, 140))
sprites_robocin2 = pygame.transform.scale(sprites_robocin2, (100, 140))
sprites_robocin3 = pygame.transform.scale(sprites_robocin3, (100, 140))
sprites_robocin4 = pygame.transform.scale(sprites_robocin4, (100, 140))
sprites_robocin5 = pygame.transform.scale(sprites_robocin5, (100, 140))


fragmentos_cracha = obstaculos_sprites['fragmentos_cracha']
foguinho = obstaculos_sprites['foguinho']
fragmentos_cracha2 = obstaculos_sprites['fragmentos_cracha2']
vidas_imagem = obstaculos_sprites['vidas_imagem']
robocin = obstaculos_sprites['robocin']

fragmentos_cracha = pygame.transform.scale(fragmentos_cracha, (30, 40))
foguinho = pygame.transform.scale(foguinho, (150, 100))
fragmentos_cracha2 = pygame.transform.scale(fragmentos_cracha, (30, 40))
vidas_imagem = pygame.transform.scale(vidas_imagem,(40,40))
robocin = pygame.transform.scale(robocin,(40,40))

musica_fundo=pygame.mixer.music.load('musicas/musica_fundo.mp3')
pygame.mixer.music.play(-1)

coleta_cracha=pygame.mixer.Sound('musicas/coleta_cracha.wav')
robocin_coletado=pygame.mixer.Sound('musicas/robocin_coletado.wav')
vida_som=pygame.mixer.Sound('musicas/vida_som.wav')
fogo_som=pygame.mixer.Sound('musicas/fogo_som.wav')


# Variáveis iniciais =========================================

tamanho_inicial = [200, 150]  # Largura e altura (largura, altura)
tamanho_atual = tamanho_inicial.copy()  # Começa com o tamanho inicial
x = 100
y = (altura / 2) - 40
velocidade_tela = 1
velocidade_objeto = 4
gravidade = 0
espaco = False
game_over = False
pontos = 0
vidas = 3
frames = 0
index = 0
existe_coracao = False
existe_robocin = False
infinito = False
primeiro_robocin = True
tempo_robocin = pygame.time.get_ticks()
tempo_rob = pygame.time.get_ticks() 
tempo = pygame.time.get_ticks()
posicao_mapa = 0
mapa = 0
fundo = backgrounds[mapa]
proximo_fundo = backgrounds[(mapa + 1)]
tempo_inicial=pygame.time.get_ticks()
tempo_total= 1*60*1000

# Inicialização dos obstáculos ================================

fragmentos = criar_fragmentos(altura, largura)
lasers = criar_lasers(altura, largura)
coracao = criar_coracao(altura, largura)
robocins = criar_robocin(altura, largura)


def mostrar_tela_inicial():
    tela.blit(tela_inicial_fundo, (0, 0))
    pygame.display.update()

def mostrar_tela_informacoes():
    tela.blit(tela_instrucoes_fundo, (0, 0))
    pygame.display.flip()

# Loop principal do jogo ======================================

def game_loop():
    global tempo_rob, espaco, game_over, pontos, x, y, gravidade, frames, index, vidas, existe_coracao, tempo, posicao_mapa, mapa, fundo, proximo_fundo, velocidade_tela, velocidade_objeto,fragmentos,lasers,ultimo_frag,ultimo_laser,tempo_inicial, robocins, existe_robocin, infinito, tempo_robocin, sprites_robocin1, sprites_robocin2, sprites_robocin3, sprites_robocin4, sprites_robocin5,musica_fundo,coleta_cracha,robocin_coletado,vida_som,fogo_som, primeiro_robocin
    
    tela_inicial = True
    tela_info = False
    fps = pygame.time.Clock()
    
    while True:
        fps.tick(100)
        if tela_inicial:
            if tela_info == False:
                mostrar_tela_inicial()

            for evento in pygame.event.get():

                # Sair do jogo ainda na tela inicial
                if evento.type == QUIT:
                    pygame.quit()
                    exit()

                # Sair da tela inicial
                elif evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_s and tela_info == False:
                        tela_inicial = False
                        x = 100
                        y = (altura / 2) - 40
                        velocidade_tela = 1
                        velocidade_objeto = 5
                        gravidade = 0
                        pontos = 0
                        vidas = 3
                        fragmentos = []
                        lasers = []
                        y_fragmento = (altura/2)-100
                        for i in range(5):
                            x_fragmento = largura + i * 40
                            fragmentos.append(pygame.Rect(x_fragmento, y_fragmento, 30, 40))
                        y_fragmento = (altura/2)-50
                        for i in range(5):
                            x_fragmento = largura + i * 40
                            fragmentos.append(pygame.Rect(x_fragmento, y_fragmento, 30, 40))
                        y_fragmento = (altura/2)
                        for i in range(5):
                            x_fragmento = largura + i * 40
                            fragmentos.append(pygame.Rect(x_fragmento, y_fragmento, 30, 40))
                    
                    if evento.key == pygame.K_i:
                        tela_info = True
                        mostrar_tela_informacoes()
                    
                    if evento.key == pygame.K_m and tela_info:
                        tela_info = False

                    
        # Inicialização/ formatação dos textos que aparecem
        else:
            tempo_atual=pygame.time.get_ticks()
            tempo_corrido=tempo_atual - tempo_inicial
            tempo_restante= tempo_total-tempo_corrido
            tela.fill(WHITE)
            texto = f': {pontos}/350'
            texto1=f': {int(vidas)}/3'

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

            if tempo_restante<=0:
                game_over=True
            if game_over:
                if pontos>=350 and tempo_restante<=0 and vidas>0:
                    tela.blit(tela_final3_fundo, (0, 0))
                    pygame.display.flip()
                    
                if tempo_restante>0:  
                    tela.blit(tela_final1_fundo, (0, 0))
                    pygame.display.flip()
                    
                if pontos<350 and tempo_restante<=0 and vidas<=0:  
                    tela.blit(tela_final2_fundo, (0, 0))
                    pygame.display.flip()
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
                        tempo_inicial +=tempo_corrido
                        tela_inicial = False
                        x = 100
                        y = (altura / 2) - 40
                        velocidade_tela = 1
                        velocidade_objeto = 5
                        gravidade = 0
                        pontos = 0
                        vidas = 3
                        fragmentos = []
                        lasers = []
                        y_fragmento = (altura/2)-100

                        for i in range(5):
                            x_fragmento = largura + i * 40
                            fragmentos.append(pygame.Rect(x_fragmento, y_fragmento, 30, 40))

                        y_fragmento = (altura/2)-50

                        for i in range(5):
                            x_fragmento = largura + i * 40
                            fragmentos.append(pygame.Rect(x_fragmento, y_fragmento, 30, 40))

                        y_fragmento = (altura/2)

                        for i in range(5):
                            x_fragmento = largura + i * 40
                            fragmentos.append(pygame.Rect(x_fragmento, y_fragmento, 30, 40))

            # Tela de Game Over
            
            if not game_over:        
                
                # Função para voar
                y, x, gravidade, frames, index = voando(y, x, gravidade, altura, sprite_baixo1, sprite_baixo2, sprite_baixo3, sprite_voando, sprite_voando2, tela, espaco, frames, index, pontos, sprite_baixo1_c, sprite_baixo2_c, sprite_baixo3_c, sprite_voando_c, sprite_voando2_c, infinito, sprites_robocin1, sprites_robocin2, sprites_robocin3, sprites_robocin4, sprites_robocin5)

                if infinito == True:
                    tempo_passado = pygame.time.get_ticks() - tempo_robocin
                    atualizar_tamanho(tamanho_atual, tempo_passado)
                    
                if infinito and tamanho_atual[0] > 0:
                    pygame.draw.rect(tela, (0, 250, 0), (1050, 100, tamanho_atual[0], 40))

                # Funções de movimentação e colisão com os fragmentos de crachá e "lasers"
                for fragmento in fragmentos[:]:

                    fragmento.x -= velocidade_objeto
                    tela.blit(fragmentos_cracha, fragmento.topleft)
                    if fragmento.right < 0:
                        fragmentos.remove(fragmento)
                fragmentos, pontos = colisao_fragmentos(fragmentos, tela, x, y, fragmentos_cracha, pontos, velocidade_objeto,coleta_cracha)
                
                for laser in lasers[:]:

                    laser.x -= velocidade_objeto
                    tela.blit(foguinho, laser.topleft)
                    if laser.right < 0:
                        lasers.remove(laser)
                lasers, game_over, vidas = colisao_laser(lasers, tela, x, y, foguinho, game_over, vidas, velocidade_objeto, infinito, fogo_som)
                
                if existe_coracao == True:

                    for coracao in coracoes[:]:
                        coracao.x -= velocidade_objeto
                        tela.blit(vidas_imagem, coracao.topleft)
                        if coracao.right < 0:
                            coracoes.remove(coracao)
                    coracoes, vidas = colisao_coracao(coracoes, tela, x, y, vidas_imagem, vidas, velocidade_objeto,vida_som)

                if existe_robocin == True:
                    
                    for robo in robocins[:]:
                        robo.x -= velocidade_objeto
                        tela.blit(robocin, robo.topleft)
                        if robo.right < 0:
                            robocins.remove(robo)

                    robocins, infinito, tempo_robocin = colisao_robocin(robocins, x, y, infinito, tempo_robocin,robocin_coletado)

                if game_over:
                    lasers.clear()
                    fragmentos.clear()
                    coracoes = []
                    robocins = []
                    
            
                tela.blit(fragmentos_cracha2, (1050, 40))
                tela.blit(texto_formatado, (1090, 40))
                tela.blit(vidas_imagem,(30,45))
                tela.blit(texto1_formatado, (80, 40))

                pygame.display.flip()



                #Excluindo as ordenadas que já possuem algum objeto problemático
                if(fragmentos):
                    ultimo_frag = fragmentos[-1].bottomright
                if(len(fragmentos)>5):
                    ultimo_frag2 = fragmentos[-6].bottomright
                if(len(fragmentos)>10):
                    ultimo_frag3 = fragmentos[-11].bottomright
                if(lasers):
                    ultimo_laser = lasers[-1].bottomright
                if(len(lasers)>1):
                    penultimo_laser = lasers[-2].bottomright
                if(existe_coracao):
                    if(coracoes):
                        ultimo_coracao = coracoes[-1].bottomright


                if len(fragmentos) <= 10:
                    listinha_de_intervalos = []
                    if(fragmentos):
                        if ultimo_frag[0]>largura-30:
                            for i in range(ultimo_frag[1]-43-40,ultimo_frag[1]+3):
                                listinha_de_intervalos.append(i)
                    if(len(fragmentos)>5):
                        if ultimo_frag2[0]>largura-30:
                            for i in range(ultimo_frag2[1]-43-40,ultimo_frag2[1]+3):
                                listinha_de_intervalos.append(i)
                    if(len(fragmentos)>10):
                        if ultimo_frag3[0]>largura-30:
                            for i in range(ultimo_frag3[1]-43-40,ultimo_frag3[1]+3):
                                listinha_de_intervalos.append(i)
                    if(lasers):
                        if ultimo_laser[0]>largura-10:
                            for i in range(ultimo_laser[1]-103-40,ultimo_laser[1]+3):
                                listinha_de_intervalos.append(i)
                    if(len(lasers)>1):
                        if penultimo_laser[0]>largura-10:
                            for i in range(penultimo_laser[1]-103-40,penultimo_laser[1]+3):
                                listinha_de_intervalos.append(i)
                    if(existe_coracao):
                        if ultimo_coracao[0]>largura-10:
                            for i in range(ultimo_coracao[1]-43-40,ultimo_coracao[1]+3):   
                                listinha_de_intervalos.append(i)


                    y_fragmento = random.randint(50, altura - 50)
                    while(y_fragmento in listinha_de_intervalos):
                        y_fragmento = random.randint(50, altura - 50)


                    for i in range(5):
                        
                        x_fragmento = largura + i * 40
                        fragmentos.append(pygame.Rect(x_fragmento, y_fragmento, 30, 40))



                if(fragmentos):
                    ultimo_frag = fragmentos[-1].bottomright
                if(len(fragmentos)>5):
                    ultimo_frag2 = fragmentos[-6].bottomright
                if(len(fragmentos)>10):
                    ultimo_frag3 = fragmentos[-11].bottomright
                if(lasers):
                    ultimo_laser = lasers[-1].bottomright
                if(len(lasers)>1):
                    penultimo_laser = lasers[-2].bottomright
                if(existe_coracao):
                    if(coracoes):
                        ultimo_coracao = coracoes[-1].bottomright

                if len(lasers) <= 2:
                    y_lasers = random.randint(50, altura - 50)
                    listinha_de_intervalos = []
                    if(fragmentos):
                        if ultimo_frag[0]>largura-30:
                            for i in range(ultimo_frag[1]-43-100,ultimo_frag[1]+3):
                                listinha_de_intervalos.append(i)
                    if (len(fragmentos)>5):
                        if ultimo_frag2[0]>largura-30:
                            for i in range(ultimo_frag2[1]-43-100,ultimo_frag2[1]+3):
                                listinha_de_intervalos.append(i)
                    if (len(fragmentos)>10):
                        if ultimo_frag3[0]>largura-30:
                            for i in range(ultimo_frag3[1]-43-100,ultimo_frag3[1]+3):
                                listinha_de_intervalos.append(i)
                    if(lasers):
                        if ultimo_laser[0]>largura-10:
                            for i in range(ultimo_laser[1]-103-100,ultimo_laser[1]+3):
                                listinha_de_intervalos.append(i)
                    if(len(lasers)>1):
                        if penultimo_laser[0]>largura-10:
                            for i in range(penultimo_laser[1]-103-100,penultimo_laser[1]+3):
                                listinha_de_intervalos.append(i)
                    if(existe_coracao):
                        if ultimo_coracao[0]>largura-10:
                            for i in range(ultimo_coracao[1]-43-100,ultimo_coracao[1]+3):   
                                listinha_de_intervalos.append(i)

                    y_lasers = random.randint(50, altura - 50)
                    while(y_lasers in listinha_de_intervalos):
                        y_lasers = random.randint(50, altura - 50)

                    for i in range(2):

                        x_lasers = largura
                        lasers.append(pygame.Rect(x_lasers, y_lasers, 150, 100))

                agora = pygame.time.get_ticks()

                if (agora - tempo) >= 5000:
                    existe_coracao = True
                    tempo = pygame.time.get_ticks()
                    coracoes = criar_coracao(altura, largura)

                if (agora - tempo_rob) >= 20000:
                    existe_robocin = True
                    tempo_rob = pygame.time.get_ticks()
                    if primeiro_robocin == False:
                        robocins = criar_robocin(altura, largura)
                    primeiro_robocin = False
                
                if (agora - tempo_robocin) >= 5000:
                    infinito = False
                
        
game_loop()