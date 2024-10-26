
#? Online Food Ordering Management System

class Order:
    def __init__(self, base_price):
        self.base_price = base_price

    def calculate_price(self):
        return self.base_price

class FoodOrder(Order):
    def calculate_price(self):
        return self.base_price + 20  # Additional service fee

class DrinkOrder(Order):
    def calculate_price(self):
        return self.base_price * 0.9  # 10% discount

class ComboOrder(Order):
    def calculate_price(self):
        return self.base_price * 0.85  # Special price for combo meals

orders = [FoodOrder(100), DrinkOrder(50), ComboOrder(200)]
for order in orders:
    print(order.calculate_price())



