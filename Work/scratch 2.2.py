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

# Composite keys
holidays = {
    (1, 1) : 'New Years',
    (3, 14) : 'Pi day',
    (9, 13) : "Programmer' s day",
}

print(holidays[1, 1])

# Sets
tech_stocks = set(['IBM','AAPL','MSFT'])
if 'IBM' in tech_stocks:
    print('IBM is in', 'tech stocsk')

names = ['IBM', 'IBM', 'AAPL','MSFT']
names = set(names) # duplicate elimination
print(names)
names.add('CSCO')
names.remove('IBM')
print(names)

# Combine sets
names_1 = set(['IBM', 'AAPL'])
names_2 = set(['CSCO','MSFT'])
names_union = names_1 | names_2
print(names_union)
names_intersection = names_1 & names_2
print(names_intersection)
