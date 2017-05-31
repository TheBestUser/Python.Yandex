class Table(object):
    def __init__(self, data):
        self._data = data

    def __str__(self):
        res = ''
        for i in self._data:
            res += str(i) + '\n'
        return res

    def __len__(self):
        return len(self._data)

    def head(self, row):
        return self._data[:row]

    def tail(self, row):
        return self._data[-row:]

    def get_table(self):
        return self._data

    def get_rows(self, *row):
        return Table(self._data[r] for r in row)

    def add_rows(self, other):
        for i in other.get_table():
            self._data.append(i)
        return self

    def add_columns(self, other):
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
