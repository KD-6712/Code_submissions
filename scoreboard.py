import pygame.font

class Scoreboard:
    """keeps track of all the information about the score"""
    def __init__(self,ai_game):
        #defining the scoretralling attributes of the game
        self.screen = ai_game.screen
        self.screen_rect =self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats


        #Font style settings
        self.text_color = (30,30,30)
        self.font= pygame.font.SysFont(None, 48)

        #inital score images
        self.prep_score()


    def prep_score(self):                        # to convert the numerical value into a string 
        """to convert the score into a string"""
        score_str =str(self.stats.score)
        """to display the score on the screen"""
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color) #pass the string to render a image


           #to show the score on the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top =20 

    
    def show_score(self): 
        """Draw score to  the screen"""
        self.screen.blit(self.score_image, self.score_rect)


