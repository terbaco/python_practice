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
from showbar import ShowBar
from single_alien import Single_Alien

def run_game():
    pygame.init()
    ai_setting = Settings()
    stats = GameStats(ai_setting)
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("AlienInvasion")

    play_button = Button(ai_setting, screen, "Play")
    ship = Ship(ai_setting, screen, stats)
    bullets = Group()
    aliens = Group()

    '''individual alien'''
    sa = Single_Alien(ai_setting, screen, 5, (100,100))
    sa.blitme()
    show_info = ShowBar(ai_setting, screen, stats,'lefttop', 'SA: ')
#   show_highest.show_bar(stats.highest_score)
#    sb = Scoreboard(ai_setting, screen, stats)
    show_highest = ShowBar(ai_setting, screen, stats, 'righttop', 'Hightest Record')
    sb = ShowBar(ai_setting, screen, stats, 'rightbottom', 'Score')
    show_level = ShowBar(ai_setting, screen, stats, 'leftbottom', 'Level')
    while True:
        gf.check_events(ai_setting, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_setting, stats, screen,ship, aliens, bullets)
            gf.update_bullets(ai_setting, screen, stats, ship, aliens, bullets)
#            gf.create_fleet(ai_setting, screen, aliens)
        gf.update_screen(ai_setting, screen, stats, sb, ship, aliens, bullets, play_button, show_level, show_highest)
        sa.update()
        show_info.show_bar(sa.x)


run_game()