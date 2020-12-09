class Stock:
    #__slots__ = ('name', '_shares', 'price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

    @property
    def cost(self):
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Shares must be an integer value")
        self._shares = value

    def sell(self, amount):
        shares = self.shares - amount
        if shares > 0:
            self.shares = shares
            print(f'You just solid {amount} shares. Current shares: {self.shares}')
        else:
            print(f'You do not have enough shares. Current shares: {self.shares}')

