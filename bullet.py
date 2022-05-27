# importing pygame
import pygame
from pygame.sprite import Sprite

"""defining the class for bullets, which manage
 bullets fired from the ship"""
class Bullet(Sprite):
    '''
    Class is defined to creat a new object bullet, which going to be used to destroy aliens, this bullets are fired from the ship
    '''
    def __init__(self, ai_game):
    #defining : class for bullets at ship's current position
        '''
        It defines the features of the bullet, like its color size and shape.
        '''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Creating a bullet at origin (0,0) and then moving it to the position of ship
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #now we need to store this position of bullet as float which can be accessed later
        self.y = float(self.rect.y)
        
    def update(self):
        '''
        This function keeps updating the position of bullet by moving it forward in the screen with specified speed
        '''
        #this update is defined to move the bullet up the screen
        #this will be keep updating the position of the bullet

        self.y -= self.settings.bullet_speed

        #updating the postion of rectangles

        self.rect.y = self.y

    def draw_bullet(self):
        '''
        This creates the bullet's shape 
        '''
        pygame.draw.rect(self.screen, self.color, self.rect)


