import sys
import pygame
import os
from ship import Ship
from settings import Settings
from bullet import Bullet

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
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        #main game driver
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._remove_old_bullets()
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
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    
    def _check_keyup_events(self, event):
        #Checks for KEY_UP and handles appropriately
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        #update images on the screen and flip to new screen
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.blitme()
        print(len(self.bullets))
        self.ship.blitme()

        pygame.display.flip()

    def _fire_bullet(self):
        self.new_bullet = Bullet(self)
        self.bullets.add(self.new_bullet)

    def _remove_old_bullets(self):
        #removes bullets that have left the visible portion of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.y < 0 or bullet.rect.y > self.settings.screen_height:
                self.bullets.remove(bullet)



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

    