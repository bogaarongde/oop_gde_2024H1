class Polygon:
    pass


class Animal:

    def __init__(self, allat_neve, allat_labak = 4):
        self.animal_name = allat_neve
        self.animal_legs = allat_labak

    def nevet_mond(self):
        print(f"A nevem: {self.animal_name}")


my_animal = Animal("Bodri")

my_animal.nevet_mond()

print(f"Az állat neve: {my_animal.animal_name} és a lábai száma {my_animal.animal_legs}")

my_animal.animal_name = "Lassie"

print(f"Az állat neve: {my_animal.animal_name} és a lábai száma {my_animal.animal_legs}")

your_animal = Animal("Gyula",6)

print(f"Az állat neve: {your_animal.animal_name} és a lábai száma {your_animal.animal_legs}")
