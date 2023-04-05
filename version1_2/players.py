from faker import Faker
from transliterate import translit
from random import randint


class Player:
    def __init__(self):
        self.player_name = ""
        self.player_stats = {}
        self.position = ""
        self.team_stats = []
        self.chosen_players = []

    # Generates a name for the player using different locales depending on country chosen
    def gen_player_name(self, country):
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
        return self.player_name

    # Outputs a random position out of 4
    def gen_player_position(self):
        num = randint(0, 3)
        positions = ["goalkeeper", "defender", "midfielder", "attacker"]
        self.position = positions[num]
        return self.position

    # Gives each player random stats depending on their position with from 0 to a max_rating variable
    def gen_player_stats(self, max_rating, academy):
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
        # Append all player data to a list of the team
        # Determine if generated player are from academy or on the transfer market
        if academy:
            self.player_stats["age"] = randint(15, 20)
        else:
            self.player_stats["age"] = randint(18, 37)
        self.player_stats[self.player_name] = self.position
        self.team_stats.append(self.player_stats)
        return self.player_stats

    def sort_age(self):
        age_sorted = sorted(self.team_stats, key=lambda x: x['age'])
        for i in age_sorted:
            print(i)

    def choose_players(self, team_stats, player_nums):
        for i in player_nums:
            self.chosen_players.append(team_stats[i])

    def print_chosen_players(self):
        for k in self.chosen_players:
            print(k)







