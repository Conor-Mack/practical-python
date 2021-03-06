#!/usr/bin/env python3
# pcost.py

from report import read_portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    return portfolio.total_cost

def main(argv):
    filename = argv[1]
    cost = portfolio_cost(filename)
    print(cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)

