import names
from random import randint


class PlayerSelection:

    def __init__(self):
        self.team_strength = 0
        self.selected_players = {}
        self.squad = ""
        self.developed_players = {}

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
            self.selected_players[players_tuples.get(i)[0][0][1]] = players_tuples.get(i)[0][1]

        for k, v in self.selected_players.items():
            print(k, v, end="||")
            self.squad += f'{k, v}||'

        player_values = []
        for value in self.selected_players.values():
            player_values.append(value)
        print()
        self.team_strength = (sum(player_values) // 11)
        return self.team_strength

    def player_development(self):
        dev_players = {}
        if dev_players == {}:
            dev_players = self.selected_players
        dev_players_keys = list(dev_players.keys())
        dev_players_values = list(dev_players.values())

        for i in range(len(dev_players)):
            dev_players[dev_players_keys[i]] = dev_players_values[i] + randint(0, 10)
            if dev_players[dev_players_keys[i]] > 100:
                dev_players[dev_players_keys[i]] = 100
        self.developed_players = dev_players
        new_team_strength = (sum(dev_players.values()) // 11)
        return new_team_strength

    def player_final_rating(self):
        for k, v in self.developed_players.items():
            print(k, v, end="||")











