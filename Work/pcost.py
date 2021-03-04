# pcost.py
#
# Exercise 1.27
total_Cost = 0.00
with open('Data/portfolio.csv', 'rt') as f:
    header = next(f)
    for line in f:
        line = line.split(',')
        total_Cost = total_Cost + (int(line[1]) * float(line[2]))
    print('Total cost', total_Cost)
    f.close()