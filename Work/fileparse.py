# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename='Data/portfolio.csv', select=['name', 'shares', 'price'], types=[str, int, float], has_headers=True, delimiter=',', silence_errors=True):
    '''
    Parse a CSV to a list of records
    '''

    # Check if select and headers false aren't used together
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

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
        for rowno, row in enumerate(rows, start=1):
            if not row: # skip empty rows
                continue
            
            if indices:
                row = [row[index] for index in indices]
            
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
