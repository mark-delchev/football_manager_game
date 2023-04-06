
class Teams:

    def __init__(self):
        self.team_aggression = 0
        self.team_attack = 0
        self.team_defense = 0
        self.team_midfield = 0
        self.team_injury = 0

    # Appends stats of each player and converts them to average team stat
    def gen_team_stats(self, team_stats):
        team_aggression_each = []
        team_attack_each = []
        team_defense_each = []
        team_midfield_each = []
        team_injury_each = []
        # Looping through each player's aggression stat and appending it to a list
        for i in range(len(team_stats)):
            team_attack_each.append(team_stats[i].get("Shooting"))
            team_midfield_each.append(team_stats[i].get("Passing"))
            team_aggression_each.append(team_stats[i].get("Aggression"))
            team_defense_each.append(team_stats[i].get("Defending"))
            team_defense_each.append(team_stats[i].get("Goalkeeping"))
            team_injury_each.append(team_stats[i].get("Injury"))
            # Removing players from different positions that don't have the required stat

            team_attack_each = [x for x in team_attack_each if x is not None]
            team_midfield_each = [x for x in team_midfield_each if x is not None]
            team_defense_each = [x for x in team_defense_each if x is not None]

        # Converting the list into a average team aggression
        self.team_aggression = sum(team_aggression_each) // len(team_aggression_each)
        self.team_attack = sum(team_attack_each) // len(team_attack_each)
        self.team_defense = sum(team_defense_each) // len(team_defense_each)
        self.team_midfield = sum(team_midfield_each) // len(team_midfield_each)
        self.team_injury = sum(team_injury_each) // len(team_injury_each)

    def print_team_stats(self):
        print("Average team stats (0-20):")
        print(f"Aggression: {self.team_aggression}")
        print(f"Injury Proneness: {self.team_injury}")
        print(f"Defense: {self.team_defense}")
        print(f"Midfield: {self.team_midfield}")
        print(f"Attack: {self.team_attack}")
