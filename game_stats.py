import pygame
import pygame.font

class GameStats:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.reset_stats()
        self.ai_game = ai_game

        #bullets image and rect
        self.bullet_img = pygame.image.load('gameart/laserBullet.png')
        self.bullet_img = pygame.transform.scale(self.bullet_img, (150,150))
        self.bullet_img_rect = self.bullet_img.get_rect()
        #lives imnages and rect
        self.lives_img = pygame.image.load('gameart/heart.png')


    def reset_stats(self):
        self.ships_left = self.settings.ships_limit
        self.fleet_drop_speed = self.settings.fleet_drop_speed
        self.fleet_rows = self.settings.starting_fleet_rows
        self.game_level = 1

    def advance_level(self):
        self.game_level += 1
        self.fleet_drop_speed += 1
        self.fleet_rows += 1

    def draw_ammo(self, ammo_available):
        for i in range(ammo_available):
            rect = self.bullet_img.get_rect()
            rect.x = self.settings.screen_width - 55 
            rect.y = self.settings.screen_height - 70 - (i * 30)
            self.screen.blit(self.bullet_img, rect)


    def draw_lives(self):
        for i in range(self.ships_left):
            rect = self.lives_img.get_rect()
            rect.x = 10
            rect.y = self.settings.screen_height - 40 - (i *30)
            self.screen.blit(self.lives_img, rect)

       
    def check_for_game_over(self):
        print(self.ships_left)
        return self.ships_left < 1
        

    def draw_game_level(self):

        level_msg = f"LEVEL {self.game_level}"

        self.width, self.height = 50, 25
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 20)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        screen_rect = self.screen.get_rect()
        self.rect.center = screen_rect.center

        self.msg_img = self.font.render(level_msg, True, self.text_color)
        self.msg_img_rect = self.msg_img.get_rect()
    
        self.msg_img_rect.x = self.settings.screen_width - 70
        self.msg_img_rect.y = 10

        self.screen.blit(self.msg_img, self.msg_img_rect)



