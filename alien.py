import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #load alien image
        self.image = pygame.image.load('gameart/alien.png')
        self.rect = self.image.get_rect()

        #start new alien near top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def update(self):
        self.rect.x += self.settings.fleet_direction        

    def update_y(self, drop):
        self.rect.y += drop
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)