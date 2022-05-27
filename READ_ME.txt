Team name: Team Pandora
Title : Alien Invasion
Team: Kartik Disawal, Jeevith Reddy, Harish M.

The game interface is quite simple as it has 
 
The players main  motive is to destroy all alien spaceships before they escape .
The three keys the player has to use are the 
Spacebar: to shoot
Left arrow : to move left
Right arrow : to move right 
Each player has 2 lives and every time he destroys an alien ship he gets rewarded with 50 point. 
And the players score will be displayed in real time during the game 
And the score board at the end of the game will show your rank in terms of medals( gold ,silver, platinum)

The code:

So we have 3 parts in this code . 

1.A ship that fires bullets : 
 
We installed a module called pygame which The pygame module contains the functionality we need to make a game
we  set a background color and store settings in a separate class where you can adjust them more easily.
We  drew  an image to the screen and give the player control over the movement of game elements. 
We  created elements that move on their own, like bullets flying up a screen, and deleted objects that are no longer needed. 



2.Making a aliens fleet
We added  a large number of identical elements to a game by creating a fleet of aliens. 
We used nested loops to create a grid of elements, and we  control the direction of objects on the screen and to respond to specific situations.
we  detected and responded to collisions between bullets  , aliens and  ship. 
we  track statistics in a game and use a game active flag to determine when the game is over ( as the player has 2 lives)





3. scoring
we created a scoreboard and we display score in real time inside the game
we stored the score at the end of the game which is marked by pressing q on keyboard
and whatever is the score after pressing the q key is stored  directly into score.txt file
now this score will be read by High_score  module .
score of each games( upon playing it multiple times) is  stored in this txt file
we use this scores and manipulate and give results using lists and dictionary.

The highscore module will show the results of your current game and will show some other results using previous games.
Please run it after playing once.


