        
from game.dealer import Dealer
from game.player import Player

class Director:
    def __init__(self):
        self.keep_playing = True
        self.score = 0
        self.dealer = Dealer()
        self.player = Player()

    def start_game(self):
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        self.dealer.get_card()
        self.dealer.player.get_highlo()
        self.dealer.check_hilo()
        self.dealer.check_points()
    

    def do_updates(self):
        points = self.dealer.points
        self.score += points


    def do_outputs(self):


        if self.dealer.keep_playing:
            choice = input("\033[1;37m Keep playing? [y/n]:\n")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False 



        
