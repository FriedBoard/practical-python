names = ['test', '123']
line = 'goog,100,1,200'
row = line.split(',')
print(row)

row.append(names[0])
row.insert(1, names[1])
print(row)

# Find position and remove value
position = row.index('goog')
print(position)
del row[position]
print(row)

# ordering
numbers = [4,5,7,2,9,1,4,8,3,2,7,0,5]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# new list
sorted_Numbers = sorted(numbers)
print(sorted_Numbers)

symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
symlist = symbols.split(',')

symlist[2] = 'CSCO'
print(symlist)

# First 3 values
print(symlist[0:4])

# Final 2
print(symlist[-2:])

mysyms = []
mysyms.append('BRK')
print(mysyms)

symlist[-2:] = mysyms
print(symlist)