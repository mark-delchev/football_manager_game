from faker import Faker
from transliterate import translit


class Name:
    def __init__(self):
        self.name = ""
        self.last_name = ""
        self.name_trans = ""

    def gen_name(self):
        fake = Faker('bg_BG')
        self.name = fake.name_male()
        name_lst = self.name.split(" ")
        if len(name_lst) > 2:
            del name_lst[0]
            self.name = " ".join(name_lst)
            self.last_name = name_lst[1]
        self.name_trans = translit(self.name, 'bg', reversed=True)
        last_name_lst = self.name_trans.split(" ")
        last_name = last_name_lst[1]
        if last_name[-1] == "a":
            last_name = last_name[:-1]
        return last_name

    def name_check(self, string):
        for i in range(100):
            self.gen_name()
            if string in self.name_trans:
                print(self.name_trans)


