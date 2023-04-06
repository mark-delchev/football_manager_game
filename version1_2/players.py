from faker import Faker
from transliterate import translit
from random import randint
from operator import itemgetter


class Player:
    def __init__(self):
        self.player_name = ""
        self.player_stats = {}
        self.position = ""
        self.team_stats = []
        self.chosen_players = []
        self.counter = 0

    # Generate player information
    def gen_player_info(self, country, max_rating, academy):
        self.counter += 1
        locale = ""
        if country == "England":
            locale = "en_UK"

        fake = Faker(locale)
        self.player_name = fake.name_male()
        # Splitting the name to remove titles like Dr. and Mr.
        name_lst = self.player_name.split(" ")
        if len(name_lst) > 2:
            del name_lst[0]
            self.player_name = " ".join(name_lst)

        num = randint(0, 3)
        positions = ["goalkeeper", "defender", "midfielder", "attacker"]
        self.position = positions[num]
        if self.position == "goalkeeper":
            self.player_stats = {"Goalkeeping": randint(0, max_rating),
                                 "Aggression": randint(0, 20),
                                 "Injury": randint(0, 20)}
        elif self.position == "defender":
            self.player_stats = {"Defending": randint(0, max_rating),
                                 "Aggression": randint(0, 20),
                                 "Injury": randint(0, 20)}
        elif self.position == "midfielder":
            self.player_stats = {"Passing": randint(0, max_rating),
                                 "Aggression": randint(0, 20),
                                 "Injury": randint(0, 20)}
        elif self.position == "attacker":
            self.player_stats = {"Shooting": randint(0, max_rating),
                                 "Aggression": randint(0, 20),
                                 "Injury": randint(0, 20)}
        if academy:
            self.player_stats["age"] = randint(15, 20)
        else:
            self.player_stats["age"] = randint(18, 37)
        self.player_stats["position"] = self.position
        self.player_stats["name"] = self.player_name
        self.player_stats["number"] = self.counter
        self.team_stats.append(self.player_stats)
        return self.player_stats

    # Sort players by age
    def sort_age(self):
        age_sorted = sorted(self.team_stats, key=lambda x: x['age'])
        for i in age_sorted:
            print(i)

    # Sort players by position
    def sort_pos(self):
        pos_sorted = sorted(self.team_stats, key=itemgetter('position'))
        for i in pos_sorted:
            print(i)

    # Choose players by their number
    def choose_players(self):
        player_nums = [int(i) for i in input().split(" ")]
        for i in range(len(self.team_stats)):
            player_num = self.team_stats[i].get("number")
            if player_num in player_nums:
                self.chosen_players.append(self.team_stats[i])
        for i in self.chosen_players:
            print(i)







