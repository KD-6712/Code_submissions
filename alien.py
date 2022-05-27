import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''
    A new class is defined to include the Aliens, this stores the informations like image of the alien, position of the alien, size of the alien and number of the alien.
    '''
    #defining a class for alien, similar to whaat we did for ship.
    #this class represents one of the alien space ship

    def __init__(self, ai_game):
        """
        Generates the alien and sets its starting position
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load the alien image and setting its position on screen
        self.image = pygame.image.load('images/alien3.bmp')
        self.rect = self.image.get_rect()

        #Creating a row of aliens, starting at top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Storing the alien's exact horizontal position on screen
        self.x = float(self.rect.x)

    def update(self):
        '''
        Through this function we are able to create multiple copy of aliens towards its right 
        '''
        #We move alien to right.
        self.x += (self.settings.alien_speed*self.settings.fleet_direction)   #each time we update aliens position and move it to right or left depending on the sign.
        self.rect.x = self.x   # update the position of aliens rect

    def check_edges(self):
        '''
        This function ensures that the aliens copied to the right won't exide the screen length
        '''
        #It will return true if alien is at the edge of screen.
        screen_rect = self.screen.get_rect()        #
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:   #the alien is at right if the right attribute is greater than right attribute of screen and similar for left side.
            return True

        
