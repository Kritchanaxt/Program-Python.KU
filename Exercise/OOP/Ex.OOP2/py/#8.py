
#? Stock Trading Management System

class StockAccount:
    def __init__(self, balance):
        self._balance = balance
        self._portfolio = {}

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("The balance must not be negative")
        else:
            self._balance = amount

    @property
    def portfolio(self):
        return self._portfolio

    def buy_stock(self, stock, amount, price):
        total_cost = amount * price
        if total_cost <= self.balance:
            self._portfolio[stock] = self._portfolio.get(stock, 0) + amount
            self.balance -= total_cost
            print(f"Buy {stock} shares for {amount} shares")
        else:
           print("Insufficient funds")

    def sell_stock(self, stock, amount, price):
        if stock in self._portfolio and self._portfolio[stock] >= amount:
            self._portfolio[stock] -= amount
            self.balance += amount * price
            print(f"Sell {stock} shares {amount}")
        else:
            print("Unable to sell shares")

# Usage
account = StockAccount(10000)
account.buy_stock("AAPL", 5, 1000)
account.sell_stock("AAPL", 3, 1200)
print(f"Balance: {account.balance}")