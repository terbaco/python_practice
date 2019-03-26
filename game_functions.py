import sys

import pygame

from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_event(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = False
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def update_bullets(ai_setting, screen, ship, aliens, bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_setting, screen, ship, aliens, bullets)
    #        print(len(bullets))

def create_new_fleet(ai_setting, screen, ship, aliens):
    length = len(aliens)
    if length > 0:
        alien = aliens.sprites()[length-1]
        distance = alien.rect.y
#        print("distance is " + str(distance) + " and alien.y is " + str(alien.rect.height))
        if distance < int(alien.rect.height * 1.2):
            return
    alien = Alien(ai_setting, screen)
    number_aliens_x = get_number_aliens_x(ai_setting, alien.rect.width)
    for alien_number in range(number_aliens_x):
        create_alien(ai_setting, screen, aliens, alien_number, 0)

def update_aliens(ai_setting, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_setting, aliens)
    aliens.update()

    width = -1
    for alien in aliens.copy():
        if alien.y >= alien.screen_rect.bottom:
            aliens.remove(alien)
        else:
            width = alien.rect.width

    if len(aliens) < get_number_aliens_x(ai_setting, width) or width == -1:
        create_new_fleet(ai_setting, screen, ship, aliens)
#        create_fleet(ai_setting, screen, ship, aliens)


#    if len(aliens) == 0:
#        create_fleet(ai_setting, screen, aliens)
    create_new_fleet(ai_setting, screen, ship, aliens)

    if pygame.sprite.spritecollideany(ship, aliens):
#        game_over(screen)
        ship_hit(ai_setting, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(ai_setting, stats, screen, ship, aliens, bullets)

def create_fleet(ai_setting, screen, ship, aliens):
        alien = Alien(ai_setting, screen)
        number_aliens_x = get_number_aliens_x(ai_setting, alien.rect.width)
        number_rows = get_number_rows(ai_setting, ship.rect.height, alien.rect.height)

        for row_number in range(number_aliens_x):
            for alien_number in range(number_aliens_x):
                create_alien(ai_setting, screen, aliens, alien_number, row_number)

#            create_alien(ai_setting, screen, aliens, alien_number_y)
        return number_aliens_x

def get_number_aliens_x(ai_setting, alien_width):
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_setting, ship_height, alien_height):
    available_space_y = ai_setting.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_setting, screen, aliens, alien_number, row_number):
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = 0
    #alien.rect.y = alien.rect.height + 2* alien.rect.height * row_number
    aliens.add(alien)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def change_fleet_direction(ai_setting, aliens):
    # drop
    for alien in aliens.sprites():
        alien.rect.y += (ai_setting.fleet_drop_speed * ai_setting.alien_speed_factor)
    #change direction
    ai_setting.fleet_direction *= -1

def check_fleet_edges(ai_setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting, aliens)
            break

def check_bullet_alien_collisions(ai_setting, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def game_over(screen):
    print("called")
    pygame.draw.rect(screen, (0,255,0), [100, 100, 50, 50])
    font = pygame.font.Font(None, 144)
    screen.fill((0,0,0))
    text = font.render("Game Over", True, (255,255,255))
    text_rect = text.get_rect()
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    screen.blit(text, [text_x, text_y])

    pygame.display.flip()
    pygame.time.wait(1000)



    screen.fill((0,0,0))
    font = pygame.font.Font(None, 72)
    text = font.render("Restart soon...", True, (255, 255, 255))
    screen.blit(text, [text_x, text_y])
    pygame.display.flip()
    pygame.time.wait(1000)

#    sys.exit()

def ship_hit(ai_setting, stats, screen, ship, aliens, bullets):

    if stats.ships_left > 0:
        stats.ships_left -= 1
    else:
        stats.game_active = False
        pygame.mouse.set_visible((True))

    aliens.empty()
    bullets.empty()

    create_new_fleet(ai_setting, screen, ship, aliens)
    ship.center_ship()

    sleep(0.5)

def check_aliens_bottom(ai_setting, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            aliens.remove(alien)
            ship_hit(ai_setting, stats, screen, ship, aliens, bullets)
            break

def check_play_button(ai_setting, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    play_button.rect = play_button.screen.get_rect()
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:

        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        create_new_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()

