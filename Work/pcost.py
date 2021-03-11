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

print(portfolio_Cost('Data/portfolio.csv'))