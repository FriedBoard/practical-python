#!/usr/bin/env python3

class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = round(float(price),2)