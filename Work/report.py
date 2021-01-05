#!/usr/bin/env python3
# report.py

from fileparse import parse_csv
from stock import Stock
from portfolio import Portfolio
import tableformat


def read_portfolio(filename, **opts):
    with open(filename, 'rt') as file:
        return Portfolio.from_csv(file, **opts)


def read_prices(filename):
    with open(filename, 'rt') as file:
        return dict(parse_csv(file, types=[str, float]))


def portfolio_report(portfolio_file, price_file, fmt="txt"):
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(price_file)

    report = make_report(portfolio, prices)

    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def make_report(portfolio, prices):
    stock_valuation = []
    for s in portfolio:
        if s.name in prices:
            old_price = float(s.price)
            new_price = float(prices[s.name])
            change = new_price - old_price
            new_stock = (s.name, s.shares, float(prices[s.name]), change)
            stock_valuation.append(new_stock)
    return stock_valuation


def print_report(report, formatter):
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        formatter.row([name, shares, price, change])


def main(args):
    portfolio_file = args[1]
    price_file = args[2]
    if len(args) == 4:
        fmt = args[3]
        portfolio_report(portfolio_file, price_file, fmt)
    else:
        portfolio_report(portfolio_file, price_file)

if __name__ == "__main__":
    import logging
    logging.basicConfig(filename='app.log', filemode='w', level = logging.WARNING)
    import sys
    main(sys.argv)