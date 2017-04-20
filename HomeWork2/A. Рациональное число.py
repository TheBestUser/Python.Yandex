import sys


def gcd(a, b):
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def lcm(a, b):
    return a * b // gcd(a, b)


class Rational(object):
    def __init__(self, numerator=0, denominator=1):
        self.numerator, self.denominator = numerator, denominator
        self.reduce()

    def __add__(self, rational):
        if self.denominator != rational.denominator:
            _lcm = lcm(self.denominator, rational.denominator)
            self.numerator *= _lcm // self.denominator
            rational.numerator *= _lcm // rational.denominator
            self.denominator = self.denominator = _lcm
        self.numerator += rational.numerator
        self.reduce()
        return self

    def __sub__(self, rational):
        if self.denominator != rational.denominator:
            _lcm = lcm(self.denominator, rational.denominator)
            self.numerator *= _lcm // self.denominator
            rational.numerator *= _lcm // rational.denominator
            self.denominator = self.denominator = _lcm
        self.numerator -= rational.numerator
        self.reduce()
        return self

    def __truediv__(self, rational):
        self.numerator *= rational.denominator
        self.denominator *= rational.numerator
        self.reduce()
        return self

    def __mul__(self, rational):
        self.numerator *= rational.numerator
        self.denominator *= rational.denominator
        self.reduce()
        return self

    def __eq__(self, rational):
        rational.reduce()
        ru = self.numerator == rational.numerator
        rd = self.denominator == rational.denominator
        return ru and rd

    def __ne__(self, rational):
        rational.reduce()
        ru = self.numerator != rational.numerator
        rd = self.denominator != rational.denominator
        return ru or rd

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def reduce(self):
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1
        while 1:
            res = gcd(self.numerator, self.denominator)
            if res == 1:
                break
            self.numerator = self.numerator // res
            self.denominator = self.denominator // res

exec(sys.stdin.read())
