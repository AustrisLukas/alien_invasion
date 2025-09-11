import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        
        #load alien image
        self.image = pygame.image.load('gameart/alien.png')
        self.rect = self.image.get_rect()

        #start new alien near top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        

