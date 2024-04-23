class Car:

    def __init__(self, make, modell, built):
        self.make = make
        self.modell = modell
        self.built = built

    def getage(self,now=2024):
        return now-self.built

    def kiir(self):
        print (f"Az autó egy {self.make} {self.modell}. Az évjárat: {self.built}. A kora {self.getage()} év")


car1 = Car("VW","Golf",2012)

print(car1.getage())
car1.kiir()