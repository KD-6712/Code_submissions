import pygame

class Ship:
    '''A class to manage the ship'''


    def __init__(self, ai_game):
        '''Initialize the ship and sets its starting position.'''
        self.screen = ai_game.screen                               #assign screen to an attribute of ship so we can easily access it in all methods in ship
        self.settings= ai_game.settings                            
        self.screen_rect = ai_game.screen.get_rect()               #treating it as a rectangular element, access the screen's rect attribute

        #load the ship image and get its rect.
        self.image = pygame.image.load('images/ship2.bmp')          # load the image
        self.rect = self.image.get_rect()                          # assign image to rect attribute so that we can use it again easily

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        
        # stores_ decimal_value_for_the_ships horizontal-value
        self.x = float(self.rect.x)
        
        #movement flags
        self.moving_right= False
        self.moving_left= False
    
    def update(self):
        """updates the ship's position based on the movement flag'"""
        """updates ship's x value(not the rectangle)"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #update rect object ship
        self.rect.x= self.x

    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)            #draws image to the screen at the position specified by self.rect
  

    def centre_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.x)