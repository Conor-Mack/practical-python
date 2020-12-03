class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        shares = self.shares - amount
        if shares > 0:
            self.shares = shares
            print(f'You just solid {amount} shares. Current shares: {self.shares}')
        else:
            print(f'You do not have enough shares. Current shares: {self.shares}')

