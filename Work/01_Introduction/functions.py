import csv
def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        totalCost = 0
        for line in rows:
            numberOfUnits = int(line[1])
            costPerUnit = float(line[2])
            totalCost = totalCost + (costPerUnit * numberOfUnits)
        return totalCost

cost = portfolio_cost('Work/Data/portfolio.csv')
print('Total Cost:', cost)