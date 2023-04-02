from players import *
from teams import *

player_instance = Player()
team_instance = Teams()

while True:
    command = input()
    if command == "stop":
        break
    elif command == "academy":
        for i in range(11):
            player_instance.gen_player_name("England")
            player_instance.gen_player_position()
            player_instance.gen_player_stats(20, True)

    elif command == "buy_player":
        for i in range(11):
            player_instance.gen_player_name("England")
            player_instance.gen_player_position()
            player_instance.gen_player_stats(20, False)

    print(player_instance.team_stats)
    team_instance.gen_team_stats(player_instance.team_stats)
    print(team_instance.team_aggression)
    print(team_instance.team_attack)
