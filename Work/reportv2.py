# report.py
#
# Exercise 2.4
import csv
import sys

def print_report(filename, pricelist):
    '''
        Takes a portfolio from read_portfolio() and prints a report
    '''
    portfolio = read_portfolio(filename, pricelist)
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in portfolio:
        print('{name:>10s} {shares:>10d} {current_price:>10.2f} {value_change:>10.2f}'.format_map(row))   

def read_portfolio(filename, pricelist):
    '''Returns the content of the portfolio file location as dict'''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            try:
                 trade = dict(zip(headers, row))
                 trade['name'] = str(trade['name'])
                 trade['shares'] = int(trade['shares'])
                 trade['price'] = round(float(trade['price']), 2)
                 trade = total_cost(trade)
                 portfolio += [trade]
              
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
        portfolio = total_value(portfolio, pricelist)
        portfolio = value_change(portfolio, pricelist)
    return(portfolio)

def total_cost(trade):
    ''' takes a trade and adds the total cost '''
    transaction_value = round(trade['shares'] * trade['price'], 2)
    trade['total_cost'] = transaction_value
    return(trade)

def total_value(portfolio, pricelist):
    ''' takes a portfolio and a pricelist and adds total_value and current_price to the trade in the portfolio '''
    price_list = prices(pricelist)
    for rowno, row in enumerate(portfolio, start=1):
        price = price_list[row['name']]
        row['total_value'] = round(float(price * row['shares']),2)  
        row['current_price'] = round(float(price_list[row['name']]),2)

    return(portfolio)

def value_change(portfolio, pricelist):
    ''' takes a portfolio and a pricelist and adds value_change to the trade portfolio.
    performs a total_value - total_cost
    '''
    price_list = prices(pricelist)
    for rowno, row in enumerate(portfolio, start=1):
        price = price_list[row['name']]
        row['value_change'] = round(float(row['total_value'] - row['total_cost']),2)
    return(portfolio)

def prices(pricelist):
    f = open(pricelist, 'r')
    price_list = {}
    rows = csv.reader(f)
    for row in rows:
        try:
            price_list[row[0]] = round(float(row[1]),2)
        except:
            continue
    return(price_list)

if len(sys.argv) == 2:
    filename = sys.argv[1]
    pricelist = sys.argv[2]
else:
    filename = 'Data/portfolio.csv'
    pricelist = 'Data/prices.csv'

print_report(filename, pricelist)