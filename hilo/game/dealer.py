import random
from game.player import Player
class Dealer:
    self.player = Player()

    def get_card():
        card = random[1,14]
        
    
    def compute_point(self):
        points = 300

        if self.player.hilo == "h":
            points += 100
        if self.player.hilo == "l":
            points += 100

        if self.player.hilo != "h":
            points -= 75
        if self.player.hilo != "l":
            points -= 75
            