import sys
from functools import wraps


def takes(*types):
    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            for t, a in zip(types, args):
                if not isinstance(a, t):
                    raise TypeError
            return func(*args, **kwargs)

        return decorated

    return decorator


exec(sys.stdin.read())
