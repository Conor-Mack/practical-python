# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    row_list = []

    with open(filename, 'rt') as f:
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

read_portfolio('Data/portfolio.csv')
