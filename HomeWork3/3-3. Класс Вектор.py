from math import sqrt


class Vector(object):
    def __init__(self, data):
        self._data = data if type(data) == tuple else tuple(data)

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str("<" + ", ".join(map(str, self._data)) + ">")

    def __add__(self, other):
        return Vector(map(lambda x, y: x + y, self._data, other.get_data()))

    def __sub__(self, other):
        return Vector(map(lambda x, y: x - y, self._data, other.get_data()))

    def __mul__(self, other):
        if type(other) == type(self):
            return sum(map(lambda x, y: x * y, self._data, other.get_data()))
        else:
            return Vector(map(lambda x: x * other, self._data))

    def __eq__(self, other):
        return self._data == other.get_data

    def __getitem__(self, index):
        return self._data[index]

    def get_data(self):
        return self._data

    def norm(self):
        return sqrt(sum(map(lambda x: x ** 2, self._data)))


a = Vector([1, 2, 3, 4, 5, 6])
b = Vector([3, 4, 5, 6, 7, 8])
c = Vector([1, 2, 3, 4, 5, 6])
print("vector a: " + str(a))
print("vector b: " + str(b))
print("norm a: " + str(a.norm()))
print("a + b = " + str(a + b))
print("a * b = " + str(a * b))
print("a * 3 = " + str(a * 3))
print(a == b)
print(a == c)
