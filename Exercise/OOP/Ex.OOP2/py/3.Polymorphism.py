
#? Online food ordering management system

class Order:
    def __init__(self, base_price):
        self.base_price = base_price

    def calculate_price(self):
        return self.base_price

class FoodOrder(Order):
    def calculate_price(self):
        return self.base_price + 20  # ค่าบริการเพิ่ม

class DrinkOrder(Order):
    def calculate_price(self):
        return self.base_price * 0.9  # ส่วนลด 10%

class ComboOrder(Order):
    def calculate_price(self):
        return self.base_price * 0.85  # ราคาพิเศษสำหรับชุดอาหาร

orders = [FoodOrder(100), DrinkOrder(50), ComboOrder(200)]
for order in orders:
    print(order.calculate_price())


