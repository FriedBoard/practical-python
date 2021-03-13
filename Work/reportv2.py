#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
import csv
import sys
import fileparse

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

def read_portfolio(filename, pricelist=None):
    '''Returns the content of the portfolio file location as dict'''
    portfolio = []
    
    f = fileparse.parse_csv(filename)
    for trade in f:
        trade = total_cost(trade)
        portfolio += [trade]

    if pricelist:
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
    price_list_rows = fileparse.parse_csv(lines=pricelist, has_headers=False, types=[str,float], select=None)
    price_list = {}
    for row in price_list_rows:
        try:
            price_list[row[0]] = round(float(row[1]),2)
        except:
            continue
    return(price_list)

def main(argv):
    if len(argv) == 2:
        try:
            portfolio_file = argv[0]
        except:
            print('No portfolio file given')
            

        try:
            price_list = argv[1]
        except:
            print('No pricelist given')
            

    else:
        portfolio_file = 'Data/portfolio.csv'
        price_list = 'Data/prices.csv'

    portfolio_lines = []
    price_lines = []

    with open(portfolio_file, 'r') as f:
        for line in f:
            line = line.rstrip()
            portfolio_lines.append(line)

    with open(price_list, 'r') as f:
        for line in f:
            line = line.rstrip()
            price_lines.append(line)

    print_report(portfolio_lines, price_lines) 

if __name__ == '__main__':
    main(sys.argv)
