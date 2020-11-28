# pcost.py
#
# Exercise 1.27

import csv
from pprint import pprint

def portfolio_cost(filename):
    row_list = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                t = {'name': record["name"], 'shares': record["shares"], 'price': record["price"]}
                row_list.append(t)
            except ValueError:
                print(f'Row {rowno}: Couldn\'t convert: {row}')
        return row_list

res = portfolio_cost('portfolio.csv')
pprint(res)