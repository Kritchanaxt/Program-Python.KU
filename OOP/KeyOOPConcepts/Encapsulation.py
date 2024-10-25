
class BankAccount:
    def __init__(self, balance):
       self.__balance = balance # Hide balance information

    def deposit(self, amount):
       self.__balance += amount

    def withdraw(self, amount):
       if amount <= self.__balance:
          self.__balance -= amount
       else:
          print("Insufficient balance")

def get_balance(self):
    return self.__balance

# Create BankAccount object
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print("Balance:", account.get_balance())