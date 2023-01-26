import random


class MatchTeams:
    def __init__(self):
        self.match_result = ""
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

    def match_simulation(self, team1, team2, team1_attack, team1_defense, team2_attack, team2_defense):

        # Assign strength values to each team for attack and defense (0-1)

        # Calculate an attack and defense bias for each team
        team1_attack_bias = team1_attack * 2.5
        team1_defense_bias = team1_defense * -2.5
        team2_attack_bias = team2_attack * 2.5
        team2_defense_bias = team2_defense * -2.5

        # Generate a random score with a bell-shaped distribution
        # and add a bias based on the team's attack and defense strength
        score1 = int(random.gauss(2.5, 1) + team1_attack_bias + team2_defense_bias)
        score2 = int(random.gauss(2.5, 1) + team2_attack_bias + team1_defense_bias)

        # Clamp the scores to the valid range (0-5)
        score1 = max(min(score1, 5), 0)
        score2 = max(min(score2, 5), 0)

        self.match_result = f"{team1} {score1} - {score2} {team2}"
        print(self.match_result)

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
        goals = 0
        points = 0
        if self.match_result.split(" ")[1] > self.match_result.split(" ")[3]:
            points += 3

        teams = [{"name": self.your_team, "points": points, "goals": goals,
                  "goal_difference": 5}]

        # Sort the teams by points in descending order
        teams = sorted(teams, key=lambda x: (x["points"], x["goal_difference"]), reverse=True)

        # Print the table
        print("{:<20} {:>10} {:>10} {:>10}".format("Team", "Points", "Goals", "Goal Diff"))
        for team in teams:
            print("{:<20} {:>10} {:>10} {:>10}".format(team["name"], team["points"], team["goals"], team["goal_difference"]))



