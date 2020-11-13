import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width,
                                  ai_settings.screen_height))
pygame.display.set_caption('Alien Invasion | Paulo Bacelar')


# Make the Play button

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    play_button = Button(ai_settings, screen, "Jogar")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets and a group of bullets
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens,
                        bullets, sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb,
                              ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets,
                             sb)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)


run_game()
