
from random import randint


class Match:
    def __init__(self):
        self.t2_goals = None
        self.t1_goals = None

    def simulate_match(self, team1_data, team2_data):
        team1 = team1_data.split("-")
        team2 = team2_data.split("-")

        team1_dict = {}
        team2_dict = {}

        team1_dict[team1[0]] = int(team1[1]) + int(randint(0, 20))
        team2_dict[team2[0]] = int(team2[1]) + int(randint(0, 20))

        team1_strength = team1_dict.get(team1[0])
        team2_strength = team2_dict.get(team2[0])
        team1_luck = 0
        team2_luck = 0

        random_event = randint(0, 1000)
        if random_event == 579:
            if team1_strength - team2_strength > 40:
                team1_luck -= 5
                team2_luck += 2
            elif 40 < (team1_strength - team2_strength) > 20:
                team1_luck -= 3
            elif team2_strength - team1_strength > 40:
                team2_luck -= 5
                team1_luck += 2
            elif 40 < (team2_strength - team1_strength) > 20:
                team2_luck -= 3


        #print(team1_strength, team2_strength)
        self.t1_goals = team1_strength // 10 - team2_strength // 10 + randint(0, 4) + team1_luck
        self.t2_goals = team2_strength // 10 - team1_strength // 10 + randint(0, 4) + team2_luck

        if self.t1_goals < 0:
            self.t1_goals = 0
        if self.t2_goals < 0:
            self.t2_goals = 0

        return(f"Final Score: {''.join([i for i in team1_dict.keys()])} {self.t1_goals} - \
{self.t2_goals} {''.join([i for i in team2_dict.keys()])}")








