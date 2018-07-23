import pytest
from calc import (add, sub, mul, div)

def test_sum():
    """Testing sum function"""
    assert add(2, 5) == 7

def test_sub():
    """Testing sub function"""
    assert sub(2, 5) == -3

def test_mul():
    """Testing mul function"""
    assert mul(2, 5) == 10

def test_div():
    """Testing div function"""
    assert div(6, 3) == 2

def test_div_by_zero():
    """Testing div function with div by 0 case"""
    with pytest.raises(ZeroDivisionError):
        div(6, 0)