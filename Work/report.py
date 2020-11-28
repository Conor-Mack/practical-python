# report.py
#
# Exercise 2.4
import csv


def dataDir(filename):
    import pathlib
    return f'{pathlib.Path(__file__).parent.absolute()}\Data\{filename}'


def read_portfolio(filename):
    row_list = []

    with open(dataDir(filename), 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        types = [str, int, float]
        for rowno, row in enumerate(rows):
            row_with_types = list(zip(types, row))
            converted_row = [func(val) for func, val in row_with_types]
            record = dict(zip(headers, converted_row))
            try:
                t = {'name': record["name"], 'shares': record["shares"], 'price': record["price"]}
                row_list.append(t)
            except ValueError:
                print(f'Row {rowno}: Couldn\'t convert: {row}')
        return row_list


def read_prices(filename):
    d = {}

    with open(dataDir(filename), 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                name, price = row
                d[name] = price
        return d

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
    print(('{dash} '.format(dash='-'*10)) * 4)
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} ${price:>10.2f} {change:>10.2f}')

def portfolio_report(portfolioFile, priceFile):
    portfolio = read_portfolio(portfolioFile)
    prices = read_prices(priceFile)

    report = make_report(portfolio, prices)
    print_report(report, ('Name', 'Shares', 'Price', 'Change'))

portfolio_report('portfolio.csv', 'prices.csv')
