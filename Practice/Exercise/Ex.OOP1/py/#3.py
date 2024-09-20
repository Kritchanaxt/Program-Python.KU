
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f}. Current balance: {self.balance:.2f} Baht.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount:.2f}. Current balance: {self.balance:.2f} Baht.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdraw amount must be positive.")

# Start 500 baht
account = BankAccount(500)

# Deposit money
account.deposit(200)

# Withdraw 100 baht
account.withdraw(100)

# Withdraw money exceeding balance
account.withdraw(1000)