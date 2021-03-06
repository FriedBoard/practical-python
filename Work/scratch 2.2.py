records = []
prices = {}

with open('Data/portfolio.csv', 'rt') as f:
    next(f) # skipping headers
    for line in f:
        row = line.split(',')
        records.append((row[0], int(row[1]), float(row[2])))

with open ('Data/prices.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        try:
            prices[row[0]] = float(row[1])
        except IndexError:
            continue

print(prices)

# Get
price = prices.get('"AXP"', 0.0)
print(price)
