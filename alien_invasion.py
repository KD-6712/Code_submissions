import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from bullet import Bullet
try:

    from alien import Alien
except ModuleNotFoundError:
    print("Please write correct module name")
try:
    import t1.py
except ModuleNotFoundError:
    print("Please write correct module name.")

"""
For playing game run alien_invasion.py Module
For Viewing the statistics and achievements run highscore.py module
For shooting aliens usr space bar
For moving the ship use right and left arrow
For quitting the game press q on your key board
For viewing details of your game and results please run the highscore.py Module
So for playing game run alien_invasion module and for seeing results run highscore module.
Please play through some powerful ide because in idle you cannot exit using "q".
"""
"""
Kartik Disawal:
Starting the game project
Adding the ship image 
Making the fleet 
Making the fleet move
Shooting Aliens 
Dynamics of movement
Highscore module
"""
"""
Harish M:
Created the Bullet module
Added the Alien image
Created the Alien module
Worked on main game module
Worked on Settings module
"""
"""
Jeevith Reddy:
coded the part of piloting the ship 
detcting the ship and alien collisions 
game resopding to aliens reaching on bottom part of the screen
button for exitting the game
fullscreen mode 
displaying the score making the score board 
updating scoreboard 

"""

# first installed pygame from cmd and then used it.
class AlienInvasion:
    '''Overall class to manage game assests and behaviour.'''
    def __init__(self):
        '''Initialize the game, and create game resources.'''
        pygame.init()                # initialize the pygame background
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)    # create a display window with fullscreen, when we create game's animation loop it updates the screen of the user.
        self.settings.screen_width = self.screen.get_rect().width           # getting the dimensions of screen from settings module.
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")                        # displaying the caption

        #creates instance to store game_stats 
        self.stats = GameStats(self)
        #create a scoreboard instance
        self.sb =Scoreboard(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):              # this is the game controller loop which updates after every input from the user.
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            if self.stats.game_active:
                
                self.ship.update()
                self._update_bullets() #update bullets after every action
                self._update_aliens()  #update the position of aliens after every action.
                self._update_screen()  # updates the screen after every action, so that the action that take place cause some change that can be shown on the scren.

    def _check_events(self):
        #Respond to keypresses and mouse events.  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()                        # exiting the game
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event) # pressing of any key, the key down event helps to take in the input of pressing the key
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)   # picking up your fingers from the key

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left= True
        elif event.key == pygame.K_q:
            try:

                with open("score.txt", "a") as f:
                    f.write(str(self.stats.score) + "\n")

            except FileNotFoundError:
                print("This file is not found")
            else:

                sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
         if event.key == pygame.K_RIGHT:
            self.ship.moving_right= False
         elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
                    

    def _fire_bullet(self):
        ''' 
        Defining the function which creates the bullets and the newly created bullets are added to group.
        The bullets are added at the place of ship 
        '''
        #creating bullets and adding it to the bullet group
        if len(self.bullets) < self.settings.bullets_allowed: 
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_aliens(self):
        '''
        We use this to call alien's update. 
        '''
        #Checking if the fleet is at the edge, then update the positions of all aliens in fleet.
        self._check_fleet_edges()
        self.aliens.update()
        #alien and collilsions 
        """The spritecollideany() function takes two arguments: a sprite and a group. The function looks for any member of the group that has collided with the sprite and stops looping through the group as soon as it finds one
member that has collided with the sprite If no collisions occur, spritecollideany() returns None and the if block at u won’t execute"""

        if pygame.sprite.spritecollideany(self.ship, self.aliens):        
            self._ship_hit()
            print("ship collided!!!") 
                                                       
        self._check_aliens_bottom()

    def _update_bullets(self):
        '''
        This function updates the position of the bullets, since this bullets are constantly moving forward.
        This function also limits the number of bullets by removing the old bullets which have gone out of the screen
        '''
        #updating the position of bullets
        self.bullets.update()
        #getting rid of old bullets that have disappeared from the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                 self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        #checking of any bullet that hit the aliens
        #If so we eliminate the alien and bullet both
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            self.stats.score += self.settings.alien_points
            self.sb.prep_score()
        if not self.aliens:
            #destroy existing bullets and create new fleets
            self.bullets.empty()
            self._create_fleet()
    
        
    def _create_fleet(self):
        # This helps to create a group of aliens, called 'fleet'
        # calling a alien into the group
        """From the first created alien, we calculate the remaining space 
        across the screen and then fill the remaining space with alien ships"""
        alien = Alien(self)
        
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        # Determining the number of rows that can be included in the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)


        # Creating a row full of aliens which are equally spaced
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
            

    def _create_alien(self, alien_number, row_number):
        '''
        This function determines/decides how many aliens should be displayed in the screen and how many rows of aliens have to be made.
        '''        
        #making a alien and adding it to the row one by one
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_number * alien_width
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


    def _update_screen(self):
        '''
        Whenever a change has occured in the code this function will keep updating the screen, so that we are able to see what and all changes are going on.
        like movement of ship etc... 
        '''
        # Update images on the screen, and flip to the new screen.
        self.screen.fill(self.settings.bg_color)   # fills the background color, the color it takes from the settings module.
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        #updating the images of aliens on the screen
        self.aliens.draw(self.screen)

        # Draw the score information
        self.sb.show_score()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _check_fleet_edges(self):
        #Action after any alien reached an edge.
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        #Cahnging fleets direction and droping entire fleet.
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """when ship  and  aliens contact"""
        if self.stats.ships_left > 0:
            

        #decreaces the number of ships left
            self.stats.ships_left -= 1

        # Get rid of  remainig ships, bullets
            self.aliens.empty()
            self.bullets.empty()

        #create a new fleet and recentre the ship's position
            self._create_fleet()
            self.ship.centre_ship()

            sleep(0.5)  #pauses the game 
        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        """ to verify if aliens reached boottom-screen """
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
    



