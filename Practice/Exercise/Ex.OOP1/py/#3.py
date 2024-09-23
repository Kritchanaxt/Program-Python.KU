
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f}.\n- Current balance: {self.balance:.2f} Baht.")
        else:
            print("- Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount:.2f}.\n- Current balance: {self.balance:.2f} Bath.")
        elif amount > self.balance:
            print("- Insufficient funds.")
        else:
            print("- Withdraw amount must be positive.")

account = BankAccount(500)
print(f"!* Bank Account *!\n- Current balance: {account.balance:.2f} Bath.")
print("-----------------------------")

deposit_amount = [200, 0]

for amount in deposit_amount:
    account.deposit(amount)

print("-----------------------------")

withdraw_amount = [100, 1000, 0]

for amount in withdraw_amount:
    account.withdraw(amount)

print("-----------------------------")
