
from read_prices import read_prices
from portfolio_cost import portfolio_cost
from pprint import pprint

def canIRetire():
    portfolio = portfolio_cost("portfolio.csv")
    prices = read_prices("prices.csv")
    breakDown = []
    for stock in portfolio:
        if stock['name'] in prices:
            old_value = float(stock['price']) * int(stock['shares'])
            new_value = float(prices[stock['name']]) * int(stock['shares'])    
            gainLoss = twoDecP(new_value - old_value)
            res = {'name': stock['name'], 'old': twoDecP(old_value), 'new': twoDecP(new_value), 'gainLoss': gainLoss}
            breakDown.append(res)

    return breakDown

twoDecP = lambda value : f'{value:0.2f}'

result = canIRetire()
pprint(result)
