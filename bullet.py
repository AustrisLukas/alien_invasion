import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_game):

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color_red
        self.out_of_bounds = False
        self.ship_rect_y = ai_game.ship.rect.y

        # create a bullet at rect[0,0] and then correct its position
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # store bullet's Y position as a float
        self.y = float(self.rect.y)


    def blitme(self):

        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):

        #move bullet Y position
        self.rect.y -= self.settings.bullet_speed

        #change bullet color from red to grey after it is fired from the ship
        if self.rect.top < (self.ship_rect_y - 10):
            self.color = self.settings.bullet_color_grey
        
        #check if bullet is out of bounds
        if self.rect.top < 0:
            self.out_of_bounds = True
        