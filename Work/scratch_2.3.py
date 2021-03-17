# f-strings
name = 'IBM'
shares = 100
price = 91.1
print(f'{name:>10s} {shares:>10d}  {price:>10.2f}')

# format map
s = {
    'name':'IBM',
    'shares':100,
    'price':91.1
}
print('{name:>10s} {shares:10d} {price:10.2f}'.format_map(s))