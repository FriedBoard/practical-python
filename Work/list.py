symlist = ['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']

if 'AAPL' in symlist:
    print(True)

# Join a list to a string

a = ','.join(symlist)
print(a)

b = ':'.join(symlist)
print(b)

c = ''.join(symlist)
print(c)