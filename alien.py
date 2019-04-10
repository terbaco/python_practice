import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, aisettings, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = aisettings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0
#        self.rect.x = self.rect.width
#        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.speed = 0.1
#        self.speed_factor = 1.0

    def update(self):
        moving = self.ai_settings.alien_speed_factor * self.speed
        self.x += (self.ai_settings.alien_speed_factor * self.speed * self.ai_settings.fleet_direction)
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