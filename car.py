class Car:

    def __init__(self, make, modell, built):
        self.make = make
        self.__modell = modell
        self.built = built

    def getage(self,now=2024):
        return now-self.built

    def __str__(self):
        return f"Az autó egy {self.make} {self.__modell}. Az évjárat: {self.built}. A kora {self.getage()} év"

    def __add__(self, other):
        if isinstance(other,Car):
            self.built = (self.built + other.built)/2
        else:
            print("Nem autó típust adtál hozzá")

car1 = Car("VW","Golf",2012)

print(car1._Car__modell)

car1._Car__modell = "Passat"

print(car1)

car2 = Car("Audi","A6",2020)


car1 + car2

print(car1)

