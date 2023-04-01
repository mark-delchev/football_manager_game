
class Teams:

    def __init__(self):
        self.team_aggression = 0
        self.team_attack = 0
        self.team_defense = 0
        self.team_injury = 0

    # Appends stats of each player and converts them to average team stat
    def gen_team_stats(self, team_stats):
        team_aggression_each = []
        team_attack_each = []
        # Looping through each player's aggression stat and appending it to a list
        for i in range(len(team_stats)):
            team_attack_each.append(team_stats[i].get("Shooting"))

        for i in range(len(team_stats)):
            team_aggression_each.append(team_stats[i].get("Aggression"))
            # Removing players from different positions that don't have the required stat
            if None in team_attack_each:
                team_attack_each.remove(None)
        # Converting the list into a average team aggression
        self.team_aggression = sum(team_aggression_each) // len(team_aggression_each)
        self.team_attack = sum(team_attack_each) // len(team_attack_each)
