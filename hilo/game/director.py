from game.dealer import Dealer
from game.player import Player

class Director:
    def __init__(self):
        self.keep_playing = True
        self.num_points = 300
        self.dealer = Dealer()
        self.player = Player()

    def start_game(self):
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs():
        self.player.get_highlo()