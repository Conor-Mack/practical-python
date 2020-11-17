import csv
from pprint import pprint

def read_prices(filename):
    d = {}
    fn = f'../Data/{filename}'

    with open(fn, 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                name, price = row
                d[name] = price
        return d


