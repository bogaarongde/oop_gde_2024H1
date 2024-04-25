class Food:

    def __init__(self,name,ar):
        self.name = name
        self.ar = ar

class Restaurant:

    def __init__(self,name):
        self.name = name
        self.menu_items = []

    def __add__(self, other_food):
        self.menu_items.append(other_food)

    def getMenuItems(self):
        for menu_item in self.menu_items:
            print(f"{menu_item.name}...........{menu_item.ar}")


food1 = Food("Pörkölt",5000)
food2 = Food("halászlé",3000)

my_restaurant = Restaurant("GDE büfé")

my_restaurant + food1
my_restaurant + food2

my_restaurant.getMenuItems()