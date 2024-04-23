class BankAccount:

    def __init__(self, kezdo_balance=0):
        self.balance = kezdo_balance

    def befizet(self, ertek):
        self.balance += ertek

    def kifizet(self, ertek):
        self.balance -= ertek

    def kiir(self):
        print(f"Egyenleg: {my_account.balance}")


my_account = BankAccount(200)

my_account.kiir()

my_account.befizet(300)

my_account.kiir()

my_account.kifizet(400)

my_account.kiir()
