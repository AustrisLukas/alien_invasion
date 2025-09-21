import pygame


class Ship:
    
    def __init__(self, ai_game):
        
        #Initialise the ship and set its starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect
        self.image = pygame.image.load('gameart/Spaceship.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom of center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        #Move the ship 3 pixels of the bottom of the screen
        self.rect.y = (self.rect.y - 3)

        self.settings = ai_game.settings
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        #draw the ship at its current location
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            if self.rect.x < (self.settings.screen_width - 50):
                self.rect.x += self.settings.ship_speed
            else:
                self.rect.x = 0
        if self.moving_left:
            if self.rect.x > 0:
                self.rect.x -= self.settings.ship_speed
            else:
                self.rect.x = (self.settings.screen_width - 50)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom


