
class Teams:

    def __init__(self):
        self.team_aggression = 0
        self.team_attack = 0
        self.team_defense = 0
        self.team_injury = 0

    def gen_team_stats(self, team_stats):
        team_aggression_each = []
        # Looping through each player's aggression stat and appending it to a list
        for i in range(len(team_stats)):
            team_aggression_each.append(team_stats[i].get("Aggression"))
        # Converting the list into a average team aggression
        self.team_aggression = sum(team_aggression_each) // len(team_aggression_each)
