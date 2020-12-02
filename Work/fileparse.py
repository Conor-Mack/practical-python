
import csv
from collections.abc import Iterable

def parse_csv(file, select=None, types=None, has_headers=False, delimiter=',', silence_errors=True):
    """
    Parse a CSV File into a list of records
    """
    if select and not has_headers:
        raise RuntimeError("Select argument requires column headers")

    if not isinstance(file, Iterable) or isinstance(file, str):
        raise TypeError("File arg must be an iterable object")

    records = []

    rows = csv.reader(file, delimiter=delimiter)

    if has_headers:
        headers = next(rows)
    else:
        headers = None

    # with open(filename) as f:
    for idx, row in enumerate(rows):

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        # for idx, row in enumerate(rows):
        if not row:
            continue
        if indices:
            row = [row[index] for index in indices]

        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except (ValueError, TypeError) as e:
                if not silence_errors:
                    print(f'Row {idx + 1}: couldn\'t convert {row}')
                    print(e)

        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)

        records.append(record)

    return records

# import gzip
# with gzip.open('Data/portfolio.csv.gz', 'rt') as file:
#     lines = parse_csv(file, types=[str, int, float], has_headers=True)
#     print(lines)