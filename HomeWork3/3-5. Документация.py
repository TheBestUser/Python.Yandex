class Table(object):
    """Table

    Available methods:
    - len(table)
    - str(table)
    - get_table(table)
    - table.head(rows)
    - table.tail(rows)
    - table.get_rows(*rows)
    - table.add_rows(other_table)
    - table.add_columns(other_table)
        
    """

    def __init__(self, data):
        """Create new table
            
        Keyword arguments:
        data -- lists with data
        
        """
        self._data = data

    def __str__(self):
        """Translate table in string"""
        res = ''
        for i in self._data:
            res += str(i) + '\n'
        return res

    def __len__(self):
        """Count number of rows and return that
        
        Keyword arguments:
        data -- lists with data
        
        """
        return len(self._data)

    def head(self, row):
        """Return the first 'row' rows as list
        
        Keyword arguments:
        row -- number row
        
        """
        return self._data[:row]

    def tail(self, row):
        """Return the last 'row' rows as list
        
        Keyword arguments:
        row -- number row
        
        """
        return self._data[-row:]

    def get_table(self):
        """Return all table as list"""
        return self._data

    def get_rows(self, *row):
        """Return current rows
        
        Keyword arguments:
        *row -- numbers rows
        
        """
        return Table(self._data[r] for r in row)

    def add_rows(self, other):
        """Add new rows from other table and return this table
        
        Keyword arguments:
        other -- table
        
        """
        for i in other.get_table():
            self._data.append(i)
        return self

    def add_columns(self, other):
        """Concatenates rows self table with rows other table and return this table

        Keyword arguments:
        other -- table

        """
        for i, j in zip(self._data, other.get_table()):
            i += j
        return self


a = Table([[5, 6], [3, 4]])
b = Table([[1, 2], [7, 8]])
print(a)
print(b)
print(a.get_rows(1))
print(a.add_rows(b))
print(a.add_columns(b))