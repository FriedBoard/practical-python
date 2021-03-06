# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename):
    '''Show what is in a portfolio and the total cost'''
    portfolio = []
    cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            try:
                holding = {
                        'name':row[0],
                        'shares':int(row[1]),
                        'price':float(row[2])
                    }
                portfolio.append(holding)
                record = dict(zip(headers, row))
                cost += int(record['shares']) * float(record['price'])
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return(portfolio, cost)

def prices():
    f = open('Data/prices.csv', 'r')
    prices = {}
    rows = csv.reader(f)
    for row in rows:
        try:
            prices[row[0]] = row[1]
        except:
            continue
    return(prices)

def trade_report(prices, portfolio):
    report = []
    for holding in portfolio:
        purchase_price = holding['shares'] * holding['price']
        value_change = holding['shares'] * float(prices[holding['name']]) - purchase_price
        report.append({
            'name':holding['name'],
            'shares':int(holding['shares']),
            'current_price':float(prices[holding['name']]),
            'purchase_price':float(holding['price']),
            'value_change':float(value_change),
        })

    return(report)
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'



total_portfolio, total_cost = read_portfolio(filename)
prices = prices()
#trade_report = trade_report(prices, total_portfolio)


print('Portfolio holdings:', total_portfolio, '\nTotal cost was:', total_cost)
'''
headers = ['Name', 'Shares', 'Price', 'Change']
print('{:>10s} {:>10s} {:>10s} {:>10s}'.format('Name', 'Shares', 'Price', 'Change'))
print('{:-^10} {:-^10} {:-^10} {:-^10}'.format('', '', '', ''))
for holding in trade_report:
    print('{name:>10s} {shares:>10d} {current_price:>10.2f} {value_change:>10.2f}'.format_map(holding))

''' 

# 2.5
portfolio = read_portfolio('Data/portfolio.csv')[0]
portfolio2 = read_portfolio('Data/portfolio2.csv')[0]
from collections import Counter
holdings = Counter()
for s in portfolio:
    holdings[s['name']] += s['shares']

holdings2 = Counter()
for s in portfolio2:
    holdings2[s['name']] += s['shares']

combined = holdings + holdings2

print(combined)

# 2.20
portfolio = read_portfolio('Data/portfolio.csv')[0]
cost = sum([s['shares'] * s['price'] for s in portfolio])
print(cost)

more100 = [ s for s in portfolio if s['shares'] > 100]
print(more100)

name_shares = [ (s['name'], s['shares']) for s in portfolio]
print(name_shares)

f = open('Data/portfoliodate.csv')
rows = csv.reader(f)
headers = next(rows)
select = ['name', 'shares', 'name']
indices = [headers.index(colname) for colname in select]
portfolio = [{colname:row[index] for colname, index in zip(select, indices)} for row in rows]
print(portfolio)