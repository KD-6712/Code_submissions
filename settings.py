class Settings:
    '''A class to store all settings for Alien Invasion.'''
    #defing the __init__ for bullets
    def __init__(self):
        '''Initialize the game settings.'''
        #screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        
        #setting of ship
        self.ship_speed = 1
        self.ship_limit = 1
    
        #creating a option to change or customise bullets
        self.bullet_speed = 2.5             # speed of bullets
        self.bullet_width = 3              # width of bullets
        self.bullet_height = 15            # height of bullets
        self.bullet_color = (230, 160, 160)  # color of bullets
        self.bullets_allowed = 10          # no. of bullets allowed

        #Alien settings
        self.alien_speed = 4             #horizontal speed
        self.fleet_drop_speed = 9      #bottom speed 
        #positive 1 represents right and -1 represents left.
        self.fleet_direction = 1           #direction of fleet 
        
        #scoreings
        self.alien_points = 50
    
    

