from itertools import product, cycle


class CartesianProduct(object):
    def __init__(self, data, n):
        self._data = cycle(product(*(data for _ in range(n))))
        self._generator = self._product_generator()
        self._cur = self._generator.__next__()

    def _product_generator(self):
        for el in self._data:
            yield el

    def next(self):
        self._cur = self._generator.__next__()

    def get_val(self):
        return self._cur

    def __str__(self):
        return str(self._cur)


X = (1, 'a')
c = CartesianProduct(X, 3)
for _ in range(10):
    print(c.get_val())
    c.next()
