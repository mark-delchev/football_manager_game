from players_v2 import *
from match_simulation_v2 import *

players_instance = PlayerSelection2()
match_instance = MatchTeams()

match_instance.choose_your_team()
players_instance.choose_players(100)
match_instance.random_team()
match_instance.match_simulation(f"{match_instance.your_team}", f"{match_instance.team}",
                                players_instance.team1_attack, players_instance.team1_defense,
                                match_instance.rating[0], match_instance.rating[1])
match_instance.get_ranking()


