import pygame, random

# Inicializando módulos de Pygame
pygame.init()

# criando um objeto pygame.time.Clock
relogio = pygame.time.Clock()

# carregando imagens
imageCat = pygame.image.load('images/cat.png')
imageCat = pygame.transform.scale(imageCat,(200,200))
imagemFundo = pygame.image.load('images/fundo.jpg')


# Definindo as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
CORTEXTO = (237, 62, 247) # cor do texto (branca)

# definindo algumas constantes
LARGURAJANELA = imagemFundo.get_width()
ALTURAJANELA = imagemFundo.get_height()
LARGURATUBARAO = imageCat.get_width()
ALTURATUBARAO = imageCat.get_height()
VEL = 6
ITERACOES = 30
VELRAIO = -15 # velocidade do raio

# Criando uma janela com o título “Olá, mundo!”
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption('PEQUENOS MIADOS')

# carregando imagens
imageCat = imageCat.convert_alpha()
imagemFundo = imagemFundo.convert_alpha()


# definindo a função moverJogador(), que registra a posição do jogador
def moverJogador(jogador, teclas, dim_janela):
    borda_esquerda = 0
    borda_direita = dim_janela[0]
    if teclas['esquerda'] and jogador['objRect'].left > borda_esquerda:
        jogador['objRect'].x -= jogador['vel']
    if teclas['direita'] and jogador['objRect'].right < borda_direita:
        jogador['objRect'].x += jogador['vel']
    
def terminar():
    # Termina o programa.
    pygame.quit()
    exit()
    
def aguardarEntrada():
    # Aguarda entrada por teclado ou clique do mouse no “x” da janela.
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminar()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    terminar()
                return

def colocarTexto(texto, fonte, janela, position):
    # Coloca na posição (x,y) da janela o texto com a fonte passados por argumento.
    objTexto = fonte.render(texto, True, CORTEXTO)
    rectTexto = objTexto.get_rect(center=position)
    janela.blit(objTexto, rectTexto)
    

# Ocultando o cursor e redimensionando a imagem de fundo.
pygame.mouse.set_visible(False)
imagemFundoRedim = pygame.transform.scale(imagemFundo,(LARGURAJANELA, ALTURAJANELA))

# Configurando a fonte.
fonte = pygame.font.Font(None, 48)

# configurando o som
pygame.mixer.music.load('surround/fundo.mp3')
#pygame.mixer.music.play(-1, 0.0)
somAtivado = True
 
# Tela de inicio.
colocarTexto('Pequenos Miados', fonte, janela, (LARGURAJANELA // 2, ALTURAJANELA // 2))
colocarTexto('Pressione uma tecla para começar.', fonte, janela, (LARGURAJANELA // 2, ALTURAJANELA // 2.5))
pygame.display.update()
aguardarEntrada()

recorde = 0
while True:
    deve_continuar = True # indica se o loop do jogo deve continuar
    
    # direções de movimentação
    # definindo o dicionario que guardará as direcoes pressionadas
    teclas = {'esquerda': False, 'direita': False}
    contador = 0 # contador de iterações
    pygame.mixer.music.play(-1, 0.0) # colocando a música de fundo
    # criando jogador
    jogador = {'objRect': pygame.Rect(300, 650, LARGURATUBARAO,ALTURATUBARAO), 'imagem': imageCat, 'vel': VEL}

    # Loop do jogo
    while deve_continuar:
        # Checando eventos
        for evento in pygame.event.get():
            # Se for um evento QUIT
            if evento.type == pygame.QUIT:
                terminar()
            # quando uma tecla é pressionada
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    terminar()
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    teclas['esquerda'] = True
                if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                    teclas['direita'] = True
                if evento.key == pygame.K_m:
                    if somAtivado:
                        pygame.mixer.music.stop()
                        somAtivado = False
                    else:
                        pygame.mixer.music.play(-1, 0.0)
                        somAtivado = True
            # quando uma tecla é solta
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    teclas['esquerda'] = False
                if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                    teclas['direita'] = False 
        
        contador += 1
        # movendo o jogador
        moverJogador(jogador, teclas, (LARGURAJANELA, ALTURAJANELA))
        # preenchendo o fundo de janela com a sua imagem
        janela.blit(imagemFundo, (0,0))
        
        # desenhando jogador
        janela.blit(jogador['imagem'], jogador['objRect'])
        
        
        # mostrando na tela tudo o que foi desenhado
        pygame.display.update()

        # limitando a 60 quadros por segundo
        relogio.tick(60)
    
    # Parando o jogo e mostrando a tela final.
    pygame.mixer.music.stop()    
    colocarTexto('Pressione uma tecla para jogar.', fonte, janela, (LARGURAJANELA / 10), (ALTURAJANELA / 2))
    pygame.display.update()
    # Aguardando entrada por teclado para reiniciar o jogo ou sair.
    aguardarEntrada()