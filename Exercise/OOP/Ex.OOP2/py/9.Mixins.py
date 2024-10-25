
#?  Restaurant management system

class Discountable:
    def apply_discount(self, price, discount):
        return price * (1 - discount)

class Loggable:
    def log(self, message):
        print(f"LOG: {message}")

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Restaurant(Discountable, Loggable):
    def __init__(self):
        self.menu = []

    def add_item(self, item):
        self.menu.append(item)
        self.log(f"add menu {item.name}")

    def remove_item(self, item_name):
        self.menu = [item for item in self.menu if item.name != item_name]
        self.log(f"delete menu {item_name}")

# Usage
restaurant = Restaurant()
item1 = MenuItem("Fried rice", 50)
item2 = MenuItem("Water", 10)

restaurant.add_item(item1)
restaurant.add_item(item2)
restaurant.remove_item("Fried rice")
