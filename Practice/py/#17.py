
#? Python_OOP03

class BankAccount:
    def __init__(self, name, balance=0):
        self.name, self.balance = name, balance

    def __lt__(self, other):
        return self.balance < other.balance
    
    def __gt__(self, other):
        return self.balance > other.balance
    
    def __repr__(self):
        return f"{self.name} has {self.balance}"
    
accounts = sorted([BankAccount("Kik", 200), BankAccount("Cathy", 300), BankAccount("NumTuk", 500)], reverse=True, key=lambda x: x.balance)

print(*accounts, sep='\n')
