import sys
import pygame
import os
from ship import Ship
from settings import Settings

class AlienInvasion:

    def __init__(self):

        self.settings = Settings()
        os.environ['SDL_VIDEO_WINDOW_POS'] = "200,-1500"
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion v0.1")
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.ship = Ship(self)
        

    def run_game(self):
        while True:
            self._check_events()
            self.ship.moveShip()
            self._update_screen() 
            self.clock.tick(60)


    def _check_events(self):
    #respond to keypress and mouse events
    #Navigate ship left or right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                
    
    
    def _update_screen(self):
        #update images on the screen and flip to new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

    