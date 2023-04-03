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
            print(player_instance.player_stats)

    elif command == "buy_player":
        for i in range(11):
            player_instance.gen_player_name("England")
            player_instance.gen_player_position()
            player_instance.gen_player_stats(20, False)
            print(player_instance.team_stats)

    elif command == "sort_age":
        unsorted_players = player_instance.team_stats
        age_sorted = sorted(unsorted_players, key=lambda x: x['age'])
        print(age_sorted)

team_instance.gen_team_stats(player_instance.team_stats)
print(team_instance.team_aggression)
print(team_instance.team_attack)
