from name_generator import *
from random import randint


class PlayerSelection2:
    def __init__(self):
        self.name_instance = Name()
        self.team1_defense = 0
        self.team1_attack = 0

    def choose_players(self, academy_level):
        goalkeepers = {}
        defenders = {}
        midfielders = {}
        attackers = {}

        # Generates 23 players
        for i in range(23):
            name = self.name_instance.gen_name()
            rating = randint(0, academy_level)
            if i < 3:
                goalkeepers[i + 1, name] = rating
            elif 3 <= i < 11:
                defenders[i + 1, name] = rating
            elif 11 <= i < 19:
                midfielders[i + 1, name] = rating
            else:
                attackers[i + 1, name] = rating

        # Sorts all players by rating
        goalkeepers_sorted = dict(sorted(goalkeepers.items(), key=lambda x: x[1], reverse=True))
        defenders_sorted = dict(sorted(defenders.items(), key=lambda x: x[1], reverse=True))
        midfielders_sorted = dict(sorted(midfielders.items(), key=lambda x: x[1], reverse=True))
        attackers_sorted = dict(sorted(attackers.items(), key=lambda x: x[1], reverse=True))

        # Choose goalkeeper
        for i, (name, rating) in enumerate(goalkeepers_sorted.items(), 1):
            if i % 5 == 0:
                print(*name, "-", rating, end='\n')
            else:
                print(*name, "-", rating, end='||')

        goalkeeper_selected = []

        while len(goalkeeper_selected) != 1:
            print()
            try:
                goalkeeper_selected = [int(i) for i in input("Choose 1 goalkeeper: ").split()]
            except ValueError:
                print("Invalid input, try again.")

        goalkeeper_selected_c = {key: value for key, value in goalkeepers.items() if key[0] in goalkeeper_selected}

        # Choose defenders
        for i, (name, rating) in enumerate(defenders_sorted.items(), 1):
            if i % 5 == 0:
                print(*name, "-", rating, end='\n')
            else:
                print(*name, "-", rating, end='||')

        defenders_selected = []

        while len(defenders_selected) != 4:
            print()
            try:
                defenders_selected = [int(i) for i in input("Choose 4 defenders: ").split()]
            except ValueError:
                print("Invalid input, try again.")

        defenders_selected_c = {key: value for key, value in defenders.items() if key[0] in defenders_selected}

        # Choose midfielders
        for i, (name, rating) in enumerate(midfielders_sorted.items(), 1):
            if i % 5 == 0:
                print(*name, "-", rating, end='\n')
            else:
                print(*name, "-", rating, end='||')

        midfielders_selected = []

        while len(midfielders_selected) != 4:
            print()
            try:
                midfielders_selected = [int(i) for i in input("Choose 4 midfielders: ").split()]
            except ValueError:
                print("Invalid input, try again.")

        midfielders_selected_c = {key: value for key, value in midfielders.items() if key[0] in midfielders_selected}

        # Choose attackers
        for i, (name, rating) in enumerate(attackers_sorted.items(), 1):
            if i % 5 == 0:
                print(*name, "-", rating, end='\n')
            else:
                print(*name, "-", rating, end='||')

        attackers_selected = []

        while len(attackers_selected) != 2:
            print()
            try:
                attackers_selected = [int(i) for i in input("Choose 2 attackers: ").split()]
            except ValueError:
                print("Invalid input, try again.")

        attackers_selected_c = {key: value for key, value in attackers.items() if key[0] in attackers_selected}

        # Print final squad
        print("Final squad:")
        for k in goalkeeper_selected_c.keys():
            print(k[1])
        for k in defenders_selected_c.keys():
            print(k[1], end="||")
        print()
        for k in midfielders_selected_c.keys():
            print(k[1], end="||")
        print()
        for k in attackers_selected_c.keys():
            print(k[1], end="||")
        print()
        self.team1_attack = (sum(attackers_selected_c.values()) +
                                  sum(midfielders_selected_c.values()) / 2) / 400
        self.team1_defense = (sum(goalkeeper_selected_c.values()) + sum(defenders_selected_c.values()) +
                                   sum(midfielders_selected_c.values()) / 2) / 700









