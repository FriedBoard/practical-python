#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27
import reportv2 as report

def portfolio_Cost(filename):
    total_Cost = 0.00
    portfolio = report.read_portfolio(filename)
    for holding in portfolio:
        total_Cost += holding['shares'] * holding['price']
    return(total_Cost)

def main(argv):
    if len(argv) == 2:
        filename = argv[1]

    else:
        filename = 'Data/portfolio.csv'
    
    portfolio_lines = []

    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            portfolio_lines.append(line)

    print(portfolio_Cost(portfolio_lines))

if __name__ == '__main__':
    import sys
    main(sys.argv)