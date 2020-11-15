
import csv

def portfolio_cost(filename):
    row_list = []
    fn = f'../Data/{filename}'
    
    with open(fn, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            t = {'name': row[0], 'shares': int(row[1]), 'price':float(row[2])}
            row_list.append(t)
        return row_list

# portfolio_cost('Work/Data/portfolio.csv')