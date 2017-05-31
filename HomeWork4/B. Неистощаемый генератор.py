import sys
from functools import wraps


def inexhaustible(func):
    class decorator:
        def __init__(self, *args, **kwargs):
            self.__args = args
            self.__kwargs = kwargs

        def __iter__(self):
            return func(*self.__args, **self.__kwargs)

    @wraps(func)
    def decorated(*args, **kwargs):
        return decorator(*args, **kwargs)

    return decorated


@inexhaustible
def some_generator():
    yield 1
    yield 2


exec(sys.stdin.read())
