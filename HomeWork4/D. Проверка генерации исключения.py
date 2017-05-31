import sys
from contextlib import contextmanager


@contextmanager
def AssertRaises(class_):
    try:
        yield
    except class_:
        pass
    except BaseException:
        raise AssertionError()
    else:
        raise AssertionError()

exec(sys.stdin.read())
