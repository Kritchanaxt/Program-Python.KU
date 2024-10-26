
#? Python_OOP04

class Product:
    def __init__(self, name, amount, price):
        self.name = name 
        self.amount = max(0, amount)
        self.price = max(0, price)

    def get_price(self, num_items):
        if num_items < 10:
           return self.price * num_items
        elif num_items >= 10 and num_items <= 99:
            return self.price * (num_items-9) * 0.9 + (self.price * 9) + (self.price * 90 *0.9)
        else:
            return self.price * (num_items-99) * 0.8 + (self.price * 9) + (self.price * 90 *0.9)


    def make_purchase(self, num_items):
        if num_items <= self.amount:
            self.amount -= num_items
            return f"{num_items} purchased, {self.amount} remaining"
        else:
            return f"Not enough stock. Available: {self.amount}"
        
products = [
    Product("Pencil", 1200, 22),
    Product("Lotion", 5000, 200),
    Product("Lipstick", 120, 1500),
    Product("Cushion", 150, 1400),
    Product("Power", 380, 2500)
    ]

quantities = [5, 10, 50, 120, 200]

data = []
for product, qty in zip(products, quantities):
    data.append([product.name, qty, f"${product.get_price(qty):.2f}", product.make_purchase(qty)])

print("-" * 60)
print(f"{'Product':<10} {'Quantity':<10} {'Total':<15} {'Status':<30}")
print("-" * 60)

for row in data:
    print(f"{row[0]:<10} {row[1]:<10} {row[2]:<15} {row[3]:<30}")
print("-" * 60)

for product, qty in zip(products, quantities):
    print(f"cost for {qty} {product.name.lower()}s: ${product.get_price(qty):.2f}")
print("-" * 60)