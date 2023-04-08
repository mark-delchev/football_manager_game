from players import *
from teams import *

player_instance = Player()
team_instance = Teams()

while True:
    command = input()
    if command == "stop":
        break
    elif command == "academy":
        player_instance.gen_country()
        # Generates 11 players from the academy
        for i in range(11):
            player_instance.gen_player_info(20, True)
            print(player_instance.player_stats)

    elif command == "choose_players":
        player_instance.choose_players()

    elif command == "buy_player":
        for i in range(11):
            player_instance.gen_player_info(20, False)
            print(player_instance.player_stats)

    elif command == "sort_age":
        player_instance.sort_age()
    elif command == "sort_pos":
        player_instance.sort_pos()


# Generates average team stats based on chosen players' abilities
team_instance.gen_team_stats(player_instance.chosen_players)

# Outputs average team stats
team_instance.print_team_stats()
