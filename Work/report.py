#!/usr/bin/env python3
# report.py

from fileparse import parse_csv

def dataDir(filename):
    import pathlib
    return f'{pathlib.Path(__file__).parent.absolute()}\Data\{filename}'


def read_portfolio(filename):
    with open(filename, 'rt') as file:
        return parse_csv(file, types=[str, int, float], has_headers=True)


def read_prices(filename):
    with open(filename, 'rt') as file:
        return dict(parse_csv(file, types=[str, float]))


def make_report(portfolio, prices):
    stock_valuation = []
    for stock in portfolio:
        if stock['name'] in prices:
            old_price = float(stock['price'])
            new_price = float(prices[stock['name']])
            change = new_price - old_price
            new_stock = (stock['name'], stock['shares'], float(prices[stock['name']]), change)
            stock_valuation.append(new_stock)
    return stock_valuation


def print_report(report, headers):
    print('%10s %10s %10s %10s' % headers)
    print(('{dash} '.format(dash='-' * 10)) * 4)
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} ${price:>10.2f} {change:>10.2f}')


def portfolio_report(portfolioFile, priceFile):
    portfolio = read_portfolio(portfolioFile)
    prices = read_prices(priceFile)

    report = make_report(portfolio, prices)
    print_report(report, ('Name', 'Shares', 'Price', 'Change'))

def main(args):
    portfolio_file = args[1]
    price_file = args[2]
    portfolio_report(portfolio_file, price_file)

if __name__ == "__main__":
    import sys
    main(sys.argv)