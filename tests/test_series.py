from math_series import __version__
from math_series.series import fibonacci,lucas,sum_series


def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci_0():
    excepted=0
    actual=fibonacci(0)
    assert excepted==actual

def test_fibonacci_1():
    excepted=1
    actual=fibonacci(1)
    assert excepted==actual

def test_fibonacci_n():

    for num in range(2,10):
        number=fibonacci(num-1) + fibonacci(num-2)

    excepted=number
    actual=fibonacci(num)
    assert excepted==actual

def test_lucas_0():
    excepted=2
    actual=lucas(0)
    assert excepted==actual

def test_lucas_1():
    excepted=1
    actual=lucas(1)
    assert excepted==actual


def test_lucas_n():

    for num in range(2,10):
        number=lucas(num-1) + lucas(num-2)

    excepted=number
    actual=lucas(num)
    assert excepted==actual


def test_sum_series_0():
    excepted=0
    actual=sum_series(0)
    assert excepted==actual

def test_sum_series_4():
    excepted=3
    actual=sum_series(4)
    assert excepted==actual