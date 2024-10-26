
#? Python_OOP04

class Investment:
    def __init__(self, principal, interest):
        self.principal = principal
        self.interest = interest

    def value_after(self, n):
        return self.principal * (1 + self.interest) ** n
    
    def __str__(self):
        return f"Principal: $ {self.principal:.2f}\nInterest: $ {self.interest:.2f}"
    
Investment = Investment(1000, 0.25)
print(Investment)
print(Investment.value_after(5))