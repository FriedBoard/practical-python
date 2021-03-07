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
        for row in rows:
            holding = {
                    'name':row[0],
                    'shares':int(row[1]),
                    'price':float(row[2])
                }
            portfolio.append(holding)

    # Calculate total cost
    for holding in portfolio:
        cost += holding['shares'] * holding['price']
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
            'shares':holding['shares'],
            'current price':prices[holding['name']],
            'purchase price':holding['price'],
            'value change':round(float(value_change), 2),
        })
    return(report)
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'



total_portfolio, total_cost = read_portfolio(filename)
prices = prices()
trade_report = trade_report(prices, total_portfolio)


print('Portfolio holdings:', total_portfolio, '\nTotal cost was:', total_cost)
print(trade_report)