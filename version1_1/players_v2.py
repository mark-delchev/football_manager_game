from name_generator import *
from random import randint


class PlayerSelection2:
    def __init__(self):
        self.players = {}
        self.name_instance = Name()

    def choose_players(self, academy_level):
        players = {}
        counter = 1
        while len(players) < 22:
            name = self.name_instance.gen_name()
            rating = randint(0, academy_level)
            players[counter, name] = rating
            counter += 1
        players_sorted = dict(sorted(players.items(), key=lambda x: x[1], reverse=True))



