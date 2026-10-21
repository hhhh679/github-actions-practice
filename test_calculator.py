# test_calculator.py
import pytest
from calculator import add,sub,mul,div

def test_add():
    assert add(1,2)==3

def test_sub():
    assert sub(5,2)==3

def test_mul():
    assert mul(2,3)==6

def test_div():
    assert div(6,2)==3
    with pytest.raises(ZeroDivisionError):
        div(2,0)
