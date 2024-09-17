import pygame

# Definindo as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
CORTEXTO = (237, 62, 247) # cor do texto (branca)

BACKGROUND = (50, 100, 200)

# definindo algumas constantes
WIDTH = 1919
HEIGHT = 858
SPRITE_X = 0
SPRITE_Y = 0
PLAYER_X = 100
PLAYER_Y = 650

class Settings():
    def setup(self, debug:bool):
        self.debug = debug
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.SPRITE_X = SPRITE_X
        self.SPRITE_Y = SPRITE_Y
        self.PLAYER_X = PLAYER_X
        self.PLAYER_Y = PLAYER_Y
        self.CORTEXTO = CORTEXTO
        self.dim_window = (WIDTH, HEIGHT)
        
        pygame.mouse.set_visible(False)
        pygame.display.set_caption('PEQUENOS MIADOS')
        
        # Configurando a fonte.
        self.fonte = pygame.font.Font(None, 48)  
        self.texto = "Pequenos Miados"  
        
        #load resources
        self.load_images()
        self.load_sounds()
       
    def load_images(self):
         # carregando imagens
        imageBackground= pygame.image.load('images/fundo.jpg').convert_alpha()
        self.imageBackground = pygame.transform.scale(imageBackground,(WIDTH, HEIGHT))
        
        self.player_all = pygame.image.load('./images/kitty.png').convert_alpha()

    def load_sounds(self):
         # configurando o som
        pygame.mixer.music.load('./surround/fundo.mp3')
        self.somAtivado = True
        
        
settings = Settings()