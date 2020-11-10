with open('Work/Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    totalCost = 0
    for line in f:
        l = line.split(',')
        numberOfUnits = int(l[1])
        costPerUnit = float(l[2])
        totalCost = totalCost + (costPerUnit * numberOfUnits)
    print('Total cost', totalCost)
