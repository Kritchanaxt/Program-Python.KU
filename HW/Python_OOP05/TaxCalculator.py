
class TaxCalculator:
    def __init__(self):
        self.tax_brackets = [
            (150000, 0), 
            (300000, 5), 
            (500000, 10), 
            (750000, 15), 
            (1000000, 20), 
            (2000000, 25), 
            (5000000, 30), 
            (float('inf'), 35)]

    def calculate_tax(self, income):
        tax, previous_limit = 0, 0
        for limit, rate in self.tax_brackets:
            if income > limit:
                tax += (limit - previous_limit) * rate / 100
                previous_limit = limit
            else:
                return tax + (income - previous_limit) * rate / 100

people = [
    ("Nida", "Wong 1", 2023, 750000), 
    ("Anny", "Wong 2", 2023, 1500000), 
    ("Bena", "Wong 3", 2023, 6500000)
    ]

calculator = TaxCalculator()


for name, last_name, year, revenue in people:
    print(f"{'-'*40}\n"
          f"{name} {last_name}, Year {year}:\n"
          f"- Revenue: {revenue:,.2f} Baht\n"
          f"- Tax: {calculator.calculate_tax(revenue):,.2f} Baht")
