
class Investment:
    def __init__(self, principal, interest):
        self.principal = max(0, principal)
        self.interest = max(0, interest)

    def value_after(self, n):
        return self.principal * (1 + self.interest) ** n 
    
    def __str__(self):
        return f"Principal: $ {self.principal:.2f}\nInterest rate: {self.interest:.2f}"
    
    
investment = Investment(1000, 0.25)
print(investment)
print(investment.value_after(5))