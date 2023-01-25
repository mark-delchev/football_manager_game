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

    def get_ranking(self):
        # Create a list of dictionaries representing the teams
        # example teams entry:
        # {"name": "Manchester United", "points": 30, "goals": 20, "goal_difference": 5},
        teams = [{"name": self.your_team, "points": 20, "goals": 20,
                  "goal_difference": 5}]

        # Sort the teams by points in descending order
        teams = sorted(teams, key=lambda x: (x["points"], x["goal_difference"]), reverse=True)

        # Print the table
        print("{:<20} {:>10} {:>10} {:>10}".format("Team", "Points", "Goals", "Goal Diff"))
        for team in teams:
            print("{:<20} {:>10} {:>10} {:>10}".format(team["name"], team["points"], team["goals"], team["goal_difference"]))



