from faker import Faker
from transliterate import translit
from random import randint
from operator import itemgetter


class Player:
    def __init__(self):
        # Stats of each individual player (a dictionary)
        self.player_stats = {}
        # Stats of all players (a list of dicts)
        self.team_stats = []
        # Stats of all chosen players
        self.chosen_players = []
        # A counter that helps generate player numbers
        self.counter = 0
        # The chosen country of origin for the club
        self.chosen_country = ""

    def gen_country(self):
        countries = ["France", "England", "Germany", "Italy", "Spain", "Russia",
                     "Norway", "Bulgaria"]
        countries_dict = {}
        counter_c = 1
        for i in countries:
            countries_dict[str(counter_c)] = i
            counter_c += 1
        print(countries_dict)
        pick_country = input("Pick your country by typing the country number: ")
        self.chosen_country = countries_dict.get(pick_country)

    # Generate player information
    def gen_player_info(self, max_rating, academy):
        self.counter += 1
        locale = ""
        if self.chosen_country == "England":
            locale = "en_UK"
        elif self.chosen_country == "France":
            locale = "fr_FR"

        fake = Faker(locale)
        player_name = fake.name_male()
        # Splitting the name to remove titles like Dr. and Mr.
        name_lst = player_name.split(" ")
        if len(name_lst) > 2:
            del name_lst[0]
            player_name = " ".join(name_lst)

        num = randint(0, 3)
        positions = ["goalkeeper", "defender", "midfielder", "attacker"]
        position = positions[num]
        if position == "goalkeeper":
            self.player_stats = {"Goalkeeping": randint(0, max_rating),
                                 "Aggression": randint(0, 20),
                                 "Injury": randint(0, 20)}
        elif position == "defender":
            self.player_stats = {"Defending": randint(0, max_rating),
                                 "Aggression": randint(0, 20),
                                 "Injury": randint(0, 20)}
        elif position == "midfielder":
            self.player_stats = {"Passing": randint(0, max_rating),
                                 "Aggression": randint(0, 20),
                                 "Injury": randint(0, 20)}
        elif position == "attacker":
            self.player_stats = {"Shooting": randint(0, max_rating),
                                 "Aggression": randint(0, 20),
                                 "Injury": randint(0, 20)}
        if academy:
            self.player_stats["age"] = randint(15, 20)
        else:
            self.player_stats["age"] = randint(18, 37)
        self.player_stats["position"] = position
        self.player_stats["name"] = player_name
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







