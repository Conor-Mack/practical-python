def print_table(data, select, formatter):
    formatter.headings(select)
    for d in data:
        row_data = [str(getattr(d, name)) for name in select]
        formatter.row(row_data)

class FormatError(Exception):
    pass

def create_formatter(fmt):
    if fmt == "txt":
        return TextTableFormatter()
    elif fmt == "csv":
        return CSVTableFormatter()
    elif fmt == "html":
        return HTMLTableFormatter()
    else:
        raise FormatError(f"{fmt} is not a valid format")

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{str(d):>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV Format
    '''

    def convert_str(self, data):
        return [str(d) for d in data]

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        str_row = self.convert_str(rowdata)
        print(','.join(str_row))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data HTML Format
    '''

    def create_row(self, data, is_header_row=True):
        cell_tags = ('<th>', '</th>') if is_header_row else ('<td>', '</td>')
        row = "<tr>"
        for idx, d in enumerate(data):
            open_tag, close_tag = cell_tags
            row += open_tag + str(d) + close_tag
            if idx == (len(data) - 1):
                row += "</tr>"
        return row

    def headings(self, headers):
        row = self.create_row(headers)
        print(row)

    def row(self, rowdata):
        row = self.create_row(rowdata, is_header_row=False)
        print(row)


