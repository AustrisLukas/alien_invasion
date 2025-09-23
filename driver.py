import sys
import pygame
import os
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from time import sleep
from button import Button

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
        self.game_stats = GameStats(self)
        self.game_active = False
        self._create_alien_fleet()
        self.start_button = Button(self,'Start Game')


    def run_game(self):
        #main game driver
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_aliens()
                self._remove_old_bullets()
                self._check_bullet_alien_collisions()
                self._check_alien_ship_collisions()
            
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
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

                
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
        if event.key == pygame.K_RETURN:
            self.game_active = True

    
    def _check_keyup_events(self, event):
        #Checks for KEY_UP and handles appropriately
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        if self.game_active:  
            #update images on the screen and flip to new screen
            #draw the background
            self.screen.fill(self.settings.bg_color)
            #draw bullets
            self.game_stats.draw_game_level()    
            for bullet in self.bullets.sprites():
                bullet.blitme()
            #draw the ship
            self.ship.blitme()
            self.aliens.draw(self.screen)
            self.game_stats.draw_ammo(self.settings.bullets_allowed - len(self.bullets))
            self.game_stats.draw_lives()
            pygame.display.flip()
        else:
            self.screen.fill(self.settings.bg_color)
            self.start_button.draw_button()
            pygame.display.flip()


    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            self.new_bullet = Bullet(self)
            self.bullets.add(self.new_bullet)
        else: 
            print('Gun overheated!')

    def _check_bullet_alien_collisions(self):
        #check if there are any colisions between two sprite groups.
        #if yes, delete bullet and alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _check_alien_ship_collisions(self):
        #check if any of the alien crafts collided with the ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._handle_ship_or_bottom_hit()


    def _handle_ship_or_bottom_hit(self):
        self.game_stats.ships_left -= 1
        self.aliens.empty()
        self.bullets.empty()
        self._create_alien_fleet()
        self.ship.center_ship()

        if self.game_stats.check_for_game_over(): self.game_active = False
        sleep(1)
            

    def _remove_old_bullets(self):
        #removes bullets that have left the visible portion of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.y < 0 or bullet.rect.y > self.settings.screen_height:
                self.bullets.remove(bullet)


    def _create_alien_fleet(self):
        alien = Alien(self)
        starting_x = alien.rect.width
        starting_y = alien.rect.height
        alien_width = alien.rect.width
        
        for i in range(self.game_stats.fleet_rows):
            j = starting_x
            while j < self.settings.screen_width - (2 * alien_width):
                #create row indentation for odd number row
                if j == starting_x and i % 2 != 0:
                    j *= 2
                    self.create_alien(j, (starting_y * i))
                #no indentation
                else: 
                    self.create_alien(j, (starting_y * i))
                #increment the j iterator 
                j = j + (2 * alien_width)

    def create_alien(self, alien_x, alien_y):
        self.new_alien = Alien(self)
        self.new_alien.rect.x = alien_x
        self.new_alien.rect.y = alien_y
        self.aliens.add(self.new_alien)


    def _update_aliens(self):
        if not self.aliens:
            self.game_stats.advance_level()
            self.bullets.empty() 
            self._create_alien_fleet()
        #check fleet edges and change moving direction if needed
        self._check_fleet_edges()
        self.aliens.update()

        
    def _check_fleet_edges(self):
        #iterate through aliens fleet and check for edge or bottom collisions. Direction change call if edge colision is detected
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            #check for collisions at the bottom
            if alien.check_bottom():
                self._handle_ship_or_bottom_hit()
                break


    def _change_fleet_direction(self):
        #change fleet direction
        self.settings.fleet_direction *= -1
        #drow down alien fleet as direction changes
        for alien in self.aliens.sprites():
            alien.update_y(self.game_stats.fleet_drop_speed)
        
    def _check_play_button(self, mouse_pos):
        #check if mouse button was clicked within the START button. If so, start game
        if self.start_button.rect.collidepoint(mouse_pos):
            self.game_stats.reset_stats()
            self.game_active = True

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

    