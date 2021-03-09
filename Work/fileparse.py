# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename='Data/portfolio.csv', select=['name', 'shares', 'price'], types=[str, int, float], has_headers=True, delimiter=','):
    '''
    Parse a CSV to a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read headers
        if has_headers:
            headers = next(rows)

        # if a selector is given, use it.
        if select:
            if has_headers:
                indices = [headers.index(colname) for colname in select]
            else:
                indices =[]
            headers = select
        else:
            indices = []
        
        records = []
        for row in rows:
            if not row: # skip empty rows
                continue
            
            if indices:
                row = [row[index] for index in indices]
            
            if types:
                row = [func(val) for func, val in zip(types, row)]

            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = row
            records.append(record)
    return(records)
