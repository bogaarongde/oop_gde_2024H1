class Person:

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def welcome(self):
        print(f"Üdvözlünk {self.name}")

    def is_adult(self, now=2024):
        return now-self.birth_year >= 18


my_person = Person("Tomi", 2000)

my_person.welcome()

if my_person.is_adult():
    print("Felnőtt")
else:
    print("Nem felnőtt")
