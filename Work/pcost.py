# pcost.py
#
# Exercise 1.27

def portfolio_Cost(filename):
    total_Cost = 0.00
    try:
        with open(filename, 'rt') as f:
            header = next(f)
            for line in f:
                line = line.split(',')
                try:
                    total_Cost = total_Cost + (int(line[1]) * float(line[2]))
                except ValueError:
                    print(line[1], 'is not an integer')
            print('Total cost', total_Cost)
            f.close()
    except FileNotFoundError:
        print(filename, "couldn't be found.")