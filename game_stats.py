class GameStats:
    """keeps the track of statictics for Alien-Invasion."""
    def __init__(self,ai_game):
        """intialize the statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True # starts A-I in an active state

    def reset_stats(self):
        """vary the statistics during the game"""
        self.ships_left = self.settings.ship_limit
        self.score=0
        

    

