class Settings():
    """ A class to store all settings for the game"""

    def __init__(self):

        self.screen_height = 800
        self.screen_width = 1200
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 4