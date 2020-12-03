#!/usr/bin/env python3
# pcost.py

from report import read_portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    return sum([p.shares * p.price for p in portfolio])

def main(argv):
    filename = argv[1]
    cost = portfolio_cost(filename)
    print(cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)

