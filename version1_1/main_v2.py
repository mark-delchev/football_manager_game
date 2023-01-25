from players_v2 import *
from match_simulation_v2 import *
from teams_v2 import *

players_instance = PlayerSelection2()
match_instance = Match2()
teams_instance = Teams2()

teams_instance.choose_your_team()
players_instance.choose_players(100)
teams_instance.random_team()
match_instance.match_simulation(f"{teams_instance.your_team}", f"{teams_instance.team}",
                                players_instance.team1_attack, players_instance.team1_defense,
                                teams_instance.rating[0], teams_instance.rating[1])
teams_instance.get_ranking()


