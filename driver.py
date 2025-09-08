import sys
import pygame
import os
from ship import Ship
from settings import Settings

class AlienInvasion:

    def __init__(self):

        #DEV mode: open game window in second screen
        os.environ['SDL_VIDEO_WINDOW_POS'] = "200,-1500"
        self.settings = Settings()
        pygame.init()
        pygame.display.set_caption("Alien Invasion v0.1")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        

    def run_game(self):
        #main game driver
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen() 
            self.clock.tick(60)


    def _check_events(self):
    #respond to keypress and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

                
    def _check_keydown_events(self,event):
        #Checks for KEY_DOWN and handles appropriately
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True        
    
    def _check_keyup_events(self, event):
        #Checks for KEY_UP and handles appropriately
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

    