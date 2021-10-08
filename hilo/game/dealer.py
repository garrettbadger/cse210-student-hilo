import random
from game.player import Player
class Dealer:
    def __init__(self):
        self.player = Player()
        self.card = []
        self.points = 300

    def get_card(self):
        self.card = random.randint[1,13]

    def check_hilo(self):
        new_card = random.randint[1,13]
        self.card.append(new_card)
        if self.card[0] > self.card[1]:
            if self.player.hilo == 'l':
                self.points += 100
            else:
                self.points -= 75
        if self.card[0] < self.card[1]:
            if self.player.hilo == 'h':
                self.points += 100
            else:
                self.points -= 75
    
  
    
            
    def check_points():
        if compute_point() == 0:
            print("Game Over")
