import random


class Teams2:
    def __init__(self):
        self.team = ""
        self.your_team = ""
        self.rating = []
        self.teams = {
            "Real Madrid": [0.97, 0.91],
            "Chelsea": [0.80, 0.80],
            "Manchester United": [0.86, 0.70],
            "Atletico Madrid": [0.73, 0.90],
            "Queens Park Rangers": [0.71, 0.64],
            "Wolverhapmton": [0.76, 0.75],
            "Torquay United": [0.29, 0.21],
            "Scunthrope United": [0.15, 0.12]
        }

    def choose_your_team(self):
        self.your_team = input("Your team name: ")

    def random_team(self):
        team, rating = random.choice(list(self.teams.items()))
        self.team = team
        self.rating = rating
