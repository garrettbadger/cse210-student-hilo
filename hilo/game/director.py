



























def do_outputs(self):
    if self.player.keep_playing():
        choice = input('Keep playing? [y/n]')
        self.keep_playing = (choice == "y")
    else:
        self.keep_playing = False 