import random
from game.player import Player
class Dealer:
    def __init__(self):
        self.player = Player()
        self.card = []
        self.points = 300
        self.keep_playing = True

    def get_card(self):
        card = random.randint(1, 13)
        self.card.append(card)
        i = len(self.card)
        # print(f"Your card is {self.card[i-1]}")
        print(f"\033[1;37m Your card is {self.card[i-1]}\n")

    def check_hilo(self):
        new_card = random.randint(1,13)
        self.card.append(new_card)
        i = len(self.card)
        print(f"Your next card is {self.card[i-1]}")
        if self.card[i-2] > self.card[i-1]:
            if self.player.hilo == 'l':
                self.points += 100
                print(f"\033[1;32m {self.points}\n")
            else:
                self.points -= 75
                print(f"\033[1;31m {self.points}\n")
        if self.card[i-2] < self.card[i-1]:
            if self.player.hilo == 'h':
                self.points += 100
                print(f"\033[1;32m {self.points}\n")
            else:
                self.points -= 75
                print(f"\033[1;31m {self.points}\n")
    
  
    def check_points(self):
        if self.points <= 0:
            self.keep_playing = False
            print("Game Over")
        else:
            self.keep_playing = True

