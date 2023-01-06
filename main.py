from match_simulation import *
from players import *

player_selection_instance = PlayerSelection()
match_instance = Match()

team_name = input()
team_strength = player_selection_instance.select_team()
print(f"Your team's rating is {team_strength} and you will be playing against\
 Real Madrid with 97 rating.")

for i in range(100):
    result = match_instance.simulate_match(f"{team_name}-{team_strength}", "Real Madrid-97")
    if match_instance.t1_goals >= match_instance.t2_goals:
        print(result)
