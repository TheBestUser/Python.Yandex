import sys


def unique(iterable):
    last = None
    for i in iterable:
        if last != i:
            yield i
            last = i
        else:
            continue


exec(sys.stdin.read())
