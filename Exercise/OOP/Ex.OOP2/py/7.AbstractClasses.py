
#? Online sales system

from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def calculate_discount(self):
        pass

class ElectronicProduct(Product):
    def calculate_discount(self):
        return self.price * 0.9  # ลด 10%

class ClothingProduct(Product):
    def __init__(self, price, quantity):
        super().__init__(price)
        self.quantity = quantity

    def calculate_discount(self):
        if self.quantity >= 3:
            return self.price * 0.8  # ลด 20% เมื่อซื้อ 3 ชิ้นขึ้นไป
        return self.price

class FurnitureProduct(Product):
    def calculate_discount(self):
        return self.price - 500  # ลด 500 บาท

# Usage
electronic = ElectronicProduct(1000)
clothing = ClothingProduct(500, 3)
furniture = FurnitureProduct(3000)

products = [electronic, clothing, furniture]
for product in products:
    print(f"Price after discount: {product.calculate_discount()}")
