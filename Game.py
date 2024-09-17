import pygame
from Settings import *

class PequenosMiados():    
    def play(self, debug:bool): 
        from Player import Player
        player = Player()
        settings.setup(debug)
        self.colocarTexto(settings.texto, settings.fonte, settings.screen, (1919//2, 858//2))
        self.aguardarEntrada()
        
        pygame.mixer.music.play(-1, 0.0)
        
        while True:
            pygame.event.pump()

            # Draw loop            
            settings.screen.blit(settings.imageBackground, (0, 0))
            player.update()
            
            pygame.display.flip()
            settings.clock.tick(3)
    def terminar(self):
        # Termina o programa.
        pygame.quit()
        exit()
        
    def aguardarEntrada(self):
        # Aguarda entrada por teclado ou clique do mouse no “x” da janela.
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    PequenosMiados.terminar()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        PequenosMiados.terminar()
                    return

    def colocarTexto(self, texto, fonte, janela, position):
        # Coloca na posição (x,y) da janela o texto com a fonte passados por argumento.
        objTexto = fonte.render(texto, True, settings.CORTEXTO)
        rectTexto = objTexto.get_rect(center=position)
        janela.blit(objTexto, rectTexto)