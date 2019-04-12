import pygame

from pygame.sprite import Sprite
from settings import Settings

class Single_Alien(Sprite):
    def __init__(self, aisettings, screen, level=1, position=None):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = aisettings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.level_private = level
        self.setting_private = Settings()
        self.setting_private.alien_speed_factor += (self.setting_private.alien_speed_factor_step * self.level_private)

        if position != None:
            self.rect.x = position[0]
            self.rect.y = position[1]
        else:
            self.rect.x = self.screen_rect.centerx
            self.rect.y = self.screen_rect.centery

#        self.rect.x = self.rect.width
#        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.speed = 0.1
        '''set alien level'''
#        self.speed_factor = 1.0

    def update(self):
        moving = self.setting_private.alien_speed_factor * self.speed
        self.x += (self.setting_private.alien_speed_factor * self.speed * self.setting_private.fleet_direction)
        self.rect.x = int(self.x + 0.5)
#        self.y = float( moving + self.y)
#        self.rect.y = int(self.y + 0.5)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True