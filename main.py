from match_simulation import *
from players import *
from teams import *

player_selection_instance = PlayerSelection()
match_instance = Match()
teams_instance = Teams()

team_name = input("Team name: ")
academy_level = 60
team_strength = player_selection_instance.select_team(academy_level)
budget = 1000000

while True:
    rival_team = teams_instance.random_team()
    result = match_instance.simulate_match(f"{team_name}-{team_strength}", f"{rival_team}")

    if team_strength < academy_level:
        team_strength = player_selection_instance.player_development()
    if match_instance.t1_goals >= match_instance.t2_goals:
        print(f"Your team's rating is {team_strength} and you will be playing against\
 {teams_instance.r_team} with {teams_instance.r_rating} rating.")
        print(result)
        budget += 1000000
        print("Congratulations!")
        print(f"Current budget: {budget:,}")
    if budget >= 5000000:
        break

player_selection_instance.player_final_rating()
"""
Levski
1 2 3 4 5 6 7 8 9 10 11
"""

