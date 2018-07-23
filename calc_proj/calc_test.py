import pytest
from calc import (add, sub, mul, div)

def test_sum():
    assert add(2, 5) == 7

def test_sub():
    assert sub(2, 5) == -3

def test_mul():
    assert mul(2, 5) == 10

def test_div():
    assert div(6, 3) == 2

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(6, 0)