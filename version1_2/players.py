from faker import Faker
from transliterate import translit
from random import randint


class Player:
    def __init__(self):
        self.player_name = ""
        self.player_stats = {}
        self.position = ""
        self.team_stats = []

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
    def gen_player_stats(self, max_rating):
        if self.position == "goalkeeper":
            self.player_stats = {"Goalkeeping": randint(0, max_rating),
                                 "Aggression": randint(0, max_rating),
                                 "Injury": randint(0, max_rating)}
        elif self.position == "defender":
            self.player_stats = {"Defending": randint(0, max_rating),
                                 "Aggression": randint(0, max_rating),
                                 "Injury": randint(0, max_rating)}
        elif self.position == "midfielder":
            self.player_stats = {"Passing": randint(0, max_rating),
                                 "Aggression": randint(0, max_rating),
                                 "Injury": randint(0, max_rating)}
        elif self.position == "attacker":
            self.player_stats = {"Shooting": randint(0, max_rating),
                                 "Aggression": randint(0, max_rating),
                                 "Injury": randint(0, max_rating)}
        # Append all player data to a list of the team
        self.player_stats[self.player_name] = self.position
        self.team_stats.append(self.player_stats)
        return self.player_stats





