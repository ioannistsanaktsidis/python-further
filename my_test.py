def addfunction(a, b):
    return a + b


def fib(n):
    return n


def test_addfunction_should_give_correct_answer_for_1_and_2():
    assert addfunction(1, 2) == 3


def test_fib_of_0_should_be_0():
    assert fib(0) == 0


def test_fib_of_1_should_be_1():
    assert fib(1) == 1
