import pygame
from pygame.locals import *
from Settings import *
from Game import settings
import sys

class Player():
    def update(self):
        self.check_keys()
        # movement
        self.animation()
        settings.screen.blit(settings.player_all, (settings.PLAYER_X, settings.PLAYER_Y), (settings.SPRITE_X * 166, settings.SPRITE_Y, 166, 166))  

    def check_keys(self):
        # check keys
        key = pygame.key.get_pressed()
        # if user clicks on cross button, close the game 
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and
                                        event.key == K_ESCAPE): 
                pygame.quit() 
                sys.exit()         
        if key[K_RIGHT] and settings.PLAYER_X < settings.dim_window[0] - 166:
            settings.PLAYER_X += 45
            settings.SPRITE_Y = 166  
        elif key[K_LEFT] and settings.PLAYER_X > 0:
            settings.PLAYER_X -= 45
            settings.SPRITE_Y = 332
        else:
            settings.SPRITE_Y = 0
    
    def animation(self):
        settings.SPRITE_X += 1
            
        if settings.SPRITE_X > 2:
            settings.SPRITE_X = 0