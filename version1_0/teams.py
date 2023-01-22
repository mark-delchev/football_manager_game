from random import randint


class Teams:
    def __init__(self):
        self.teams = {}
        self.r_team = ""
        self.r_rating = 0

    def random_team(self):
        self.teams = {
            "Real Madrid": 97,
            "Chelsea": 87,
            "Manchester United": 86,
            "Atletico Madrid": 83,
            "Queens Park Rangers": 71,
            "Wolverhapmton": 76,
            "Torquay United": 29,
            "Scunthrope United": 15,

        }
        teams = []
        ratings = []
        for team in self.teams.keys():
            teams.append(team)
        for rating in self.teams.values():
            ratings.append(rating)
        rand_num = randint(0, len(teams))
        self.r_team = teams[rand_num - 1]
        self.r_rating = ratings[rand_num - 1]
        return f"{teams[rand_num - 1]}-{ratings[rand_num - 1]}"


