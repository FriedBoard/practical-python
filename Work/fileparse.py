# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float], has_headers=True, delimiter=',',silence_errors=True):
    '''
    Parse a list to a list or dict of records
    '''

    # Check if select and headers false aren't used together
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')


    # Read headers
    if has_headers:
        headers = lines[0].split(delimiter)
        lines.remove(lines[0])

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
    for rowno, row in enumerate(lines, start=1):
        if not row: # skip empty rows
            continue

        row = row.split(delimiter)
        try:
            if types:
                row = [func(val) for func, val in zip(types, row)]

            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = row
            records.append(record)
        except ValueError as e:
            if silence_errors:
                continue
            else:
                print('row {}, {} has problems'.format(rowno, row))
                print('row {} problem: {}'.format(rowno, e))
    return(records)
'''
with open('Data/portfolio.csv') as f:
    lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1']
    print(parse_csv(lines))
'''