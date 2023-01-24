import random


class Match2:
    def __init__(self):
        pass

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

        match_result = f"{team1} {score1} - {score2} {team2}"
        print(match_result)


