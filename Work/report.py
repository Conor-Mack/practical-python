# report.py
#
# Exercise 2.4
import csv

def portfolio_cost(filename):
    row_list = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            t = (row[0], int(row[1]), float(row[2]))
            row_list.append(t)
        return row_list

# portfolio_cost('Work/Data/portfolio.csv')