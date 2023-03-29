from faker import Faker
from transliterate import translit


class PlayerNames:
    def __init__(self):
        self.player_name = ""

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



