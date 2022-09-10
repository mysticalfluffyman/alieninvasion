import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    gamesettings = Settings()
    screen = pygame.display.set_mode((gamesettings.screen_width,gamesettings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(gamesettings,screen)
    # Make a group to store bullets in.
    bullets = Group() 
    while True:
        gf.check_events(gamesettings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(gamesettings,screen,ship, bullets)

run_game()