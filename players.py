import names
from random import randint


class PlayerSelection:

    def __init__(self):
        self.team_strength = 0

    def select_team(self, academy_level):
        players = {}
        selected_players = {}
        counter_0 = 1
        while True:
            if len(players.keys()) == 22:
                break
            name = names.get_last_name()
            rating = randint(0, academy_level)
            players[counter_0, name] = rating
            counter_0 += 1
        players_sorted = sorted(players.items(), key=lambda x: x[1], reverse=True)
        counter = 1
        for k, v in players_sorted:
            if counter % 5 != 0:
                print(f"{k}-{v}", end="      ")
            else:
                print(f"{k}-{v}")
            counter += 1
        print()
        print("Choose the players you like by writing their number separated by a whitespace. You can \
choose exactly 11 players.")
        while True:
            chosen_players = [int(i) for i in input().split(" ")]
            if len(chosen_players) > 11:
                print("You have chosen more than 11 players try again.")
            elif len(chosen_players) < 11:
                print("You have chosen less than 11 players try again")
            else:
                break

        players_tuples = {}

        for item in players_sorted:
            key = item[0][0]
            players_tuples.setdefault(key, [])
            players_tuples[key].append(item)

        for i in chosen_players:
            selected_players[players_tuples.get(i)[0][0][1]] = players_tuples.get(i)[0][1]

        for k, v in selected_players.items():
            print(k, v, end="||")

        player_values = []
        for value in selected_players.values():
            player_values.append(value)
        print()
        self.team_strength = (sum(player_values) // 11)
        return self.team_strength


