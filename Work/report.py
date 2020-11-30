from fileparse import parse_csv


def dataDir(filename):
    import pathlib
    return f'{pathlib.Path(__file__).parent.absolute()}\Data\{filename}'


def read_portfolio(filename):
    return parse_csv(filename, types=[str, int, float], has_headers=True)


def read_prices(filename):
    return dict(parse_csv(filename, types=[str, float]))


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
