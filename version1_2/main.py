from players import *
from teams import *
from operator import itemgetter

player_instance = Player()
team_instance = Teams()

while True:
    command = input()
    if command == "stop":
        break
    elif command == "academy":
        # Generates 11 players from the academy
        for i in range(11):
            player_instance.gen_player_name("England")
            player_instance.gen_player_position()
            player_instance.gen_player_stats(20, True)
            print(player_instance.player_stats)
        # Choose players by typing their numbers by the order they appear
        try:
            chosen_players = [int(i) for i in input().split(" ")]
            # Selects players based on numbers input
            player_instance.choose_players(player_instance.team_stats, chosen_players)
            player_instance.print_chosen_players()
        except ValueError:
            command = input()
    elif command == "buy_player":
        for i in range(11):
            player_instance.gen_player_name("England")
            player_instance.gen_player_position()
            player_instance.gen_player_stats(20, False)
            print(player_instance.team_stats)

    elif command == "sort_age":
        # Sorts players by age using lambda
        unsorted_players = player_instance.player_stats
        age_sorted = sorted(unsorted_players, key=lambda x: x['age'])
        for i in range(len(age_sorted)):
            print(age_sorted[i])
    elif command == "sort_position":
        unsorted_players = player_instance.player_stats
        pos_sorted = sorted(unsorted_players, key=itemgetter('name'))
        for i in range(len(pos_sorted)):
            print(pos_sorted[i])

# Generates average team stats based on chosen players' abilites
team_instance.gen_team_stats(player_instance.chosen_players)
# Outputs average team stats
team_instance.print_team_stats()
