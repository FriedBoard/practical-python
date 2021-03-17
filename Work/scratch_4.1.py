import stock
a = stock.Stock('GOOG', 100, 490.10)
b = stock.Stock('AAPL', 50, 122.34)
c = stock.Stock('IBM', 75, 91.75)

stocks = [a, b, c]
for s in stocks:
    print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}')