import sys
import pygame
import os
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien

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
        self.aliens = pygame.sprite.Group()

        self._create_alien_fleet()


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
        #draw the background
        self.screen.fill(self.settings.bg_color)
        #draw bullets
        for bullet in self.bullets.sprites():
            bullet.blitme()
        #draw the ship
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            self.new_bullet = Bullet(self)
            self.bullets.add(self.new_bullet)
        else: 
            print('Gun overheated!')

    

    def _remove_old_bullets(self):
        #removes bullets that have left the visible portion of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.y < 0 or bullet.rect.y > self.settings.screen_height:
                self.bullets.remove(bullet)


    def _create_alien_fleet(self):

        alien = Alien(self)
        alien_width = alien.rect.width

        current_x = alien_width
        while (current_x < self.settings.screen_width - (2 * alien_width)):

            alien = Alien(self)
            alien.rect.x = current_x
            self.aliens.add(alien)
            current_x += 2 * alien_width





        

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

    