email_address = None
if email_address:
    print(email_address)


# tuples
s = ('goog', 100, 490.1)
s = 'goog', 100, 490.1

name = s[0]
shares = s[1]
price = s[2]

print(name, shares, price)

s = (s[0], 75, s[2])
print(s)

# Tuple unpacking
name, shares, price = s
print(name, shares, price)

# Dictionaries
s = {
    'name': 'goog',
    'shares': 100,
    'price': 490.1
}
print(s)

s['shares'] = 75
s['date'] = '6/6/2007'
print(s)

del s['date']
print(s)

import csv
f = open('Data/portfolio.csv')
rows = csv.reader(f)
next(rows)
row = next(rows)
print(row)
t = (row[0], int(row[1]), float(row[2]))
print(t)
cost = t[1] * t[2]
print(f'{cost:0.2f}')

d = {
    'name' : row[0],
    'shares' : int(row[1]),
    'price' : float(row[2])
}
cost = d['shares'] * d['price']
print(f'{cost:0.2f}')

# List of dict keys
dict_list = list(d)
print(dict_list)

for k in dict_list:
    print(k, '=', d[k])

# items
items = d.items()
print(items)

for k, v in d.items():
    print(k, '=', v)

# Create dict from items
print(dict(items))