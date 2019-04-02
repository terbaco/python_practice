import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("AlienInvasion")

    play_button = Button(ai_setting, screen, "Play")
    ship = Ship(ai_setting, screen)
    bullets = Group()
    aliens = Group()

    stats = GameStats(ai_setting)
    sb = Scoreboard(ai_setting, screen, stats)
    while True:
        gf.check_events(ai_setting, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_setting, stats, screen,ship, aliens, bullets)
            gf.update_bullets(ai_setting, screen, stats, ship, aliens, bullets)
#            gf.create_fleet(ai_setting, screen, aliens)
        gf.update_screen(ai_setting, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()