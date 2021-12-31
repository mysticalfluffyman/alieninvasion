import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    gamesettings = Settings()
    screen = pygame.display.set_mode((gamesettings.screen_width,gamesettings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    alienship = Ship(gamesettings,screen)

    while True:
        gf.check_events(alienship)
        alienship.update()
        gf.update_screen(gamesettings,screen,alienship)

run_game()