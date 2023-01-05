import names
from random import randint

players = {}
selected_players = {}

while True:
    if len(players.keys()) == 22:
        break
    name = names.get_last_name()
    rating = randint(0, 100)
    players[name] = rating

counter = 1
for k, v in players.items():
    if counter % 5 != 0:
        print(f"{k}-{v}", end="      ")
    else:
        print(f"{k}-{v}")
    counter += 1
print()
print("Choose the player you like by writing their names seperated by a comma. You can \
choose exactly 11 players.")
chosen_players = input().split(", ")
for player in chosen_players:
    selected_players[player] = players.get(player)

print(selected_players)


