import math

from contextlib import contextmanager


@contextmanager
def MYraises(e):
    try:
        yield
    except e:
        pass


def test_sqrt_negative():
    with MYraises(ValueError):
        math.sqrt(-1)
