from Player import Player 
from Settings import Settings

class Game:
    def __init__(self, player_1=Player(), player_2=Player(), settings=Settings()):
        self.player_1 = player_1
        self.player_2 = player_2
        self.settings = settings 

    def winner(self):
        if self.player_1._health < 1:
            return f"{self.player_2.name} Wins!"
        elif self.player_2._health < 1:
            return f"{self.player_1.name} Wins!"
        else:
            return "Continue."

    @staticmethod
    def start():
        print("Let the best prevail... Begin!")
        pass

    def timer(self): 
        while self.settings.time > 0:
            self.settings.time -= 1
            return self.settings.time


