import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_game):

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

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
        self.rect.y -= self.settings.bullet_speed