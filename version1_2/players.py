from faker import Faker
from transliterate import translit
from random import randint


class Player:
    def __init__(self):
        self.player_name = ""
        self.player_stats = {}
        self.position = ""

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

    def gen_player_position(self):
        num = randint(0, 4)
        positions = ["goalkeeper", "defender", "midfielder", "attacker"]
        self.position = positions[num]
        return self.position

    def gen_player_stats(self, max_rating):
        if self.position == "goalkeeper":
            self.player_stats = {"Goalkeeping": randint(0, max_rating),
                                 "Aggression": randint(0, max_rating),
                                 "Injury": randint(0, max_rating)}
            return self.player_stats





