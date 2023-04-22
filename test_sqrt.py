import pytest
from sqrt import sqrt

def test_sqrt_positive_number():
    assert sqrt(4) == 2.0
    assert sqrt(9) == 3.0

def test_sqrt_zero():
    assert sqrt(0) == 0.0

def test_sqrt_negative_number():
    with pytest.raises(ValueError):
        sqrt(-1)
    with pytest.raises(ValueError):
        sqrt(-4)