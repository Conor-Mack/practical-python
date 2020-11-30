
from report import read_portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    return sum([p['shares'] * p["price"] for p in portfolio])


