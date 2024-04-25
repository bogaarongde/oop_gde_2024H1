class Person:

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def welcome(self):
        print(f"Üdvözlünk {self.name}")

    def is_adult(self, now=2024):
        return now-self.birth_year >= 18


input_name = input("Mi az ember neve: ")

while True:
    input_birth_year = input("Mikor született: ")

    try:
        input_birth_year_integer = int(input_birth_year)
        break
    except ValueError:
        print("Nem szám, amit beírtál, írj be újat")


my_person = Person(input_name, input_birth_year_integer)

my_person.welcome()

if my_person.is_adult():
    print("Felnőtt")
else:
    print("Nem felnőtt")
