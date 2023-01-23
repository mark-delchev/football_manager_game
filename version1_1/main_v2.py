from players_v2 import *
from match_simulation_v2 import *

players_instance = PlayerSelection2()

players_instance.choose_players(100)
match_instance = Match2()
match_instance.match_simulation("Levski", "CSKA", players_instance.team1_attack, players_instance.team1_defense,
                                0, 0)

