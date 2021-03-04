def sumcount(n):
    '''
    Returns the sum of n
    '''

    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

a = sumcount(100)
print(a)
'''
import math
x = math.sqrt(10)
print(x)

import urllib.request
u = urllib.request.urlopen('http://www.python.org/')
data = u.read()
print(data)
'''
with open('Data/portfolio.csv', 'rt') as file:
    headers = next(file)
    for line in file:
        fields = line.split(',')
        try:
            shares = int(fields[1])
            print(shares)
        except ValueError:
            print("Couldn't parse", line)