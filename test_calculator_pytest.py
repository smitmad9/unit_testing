import pytest
import calculator

def test_addition():
    assert calculator.addition(10, 1) == 11
    assert calculator.addition(-10, 1) == -9
    assert calculator.addition(0, 1) == 1
    assert calculator.addition(-1, 1) == 0
    assert calculator.addition(1.5, 1) == 2.5

def test_subtraction():
    assert calculator.subtraction(10, 1) == 9
    assert calculator.subtraction(-10, 1) == -11
    assert calculator.subtraction(0,1) == -1
    assert calculator.subtraction(-1, 1) == -2
    assert calculator.subtraction(1.5, 1) == 0.5

def test_multiplication():
    assert calculator.multiplication(10, 2) == 20
    assert calculator.multiplication(0, 1) == 0
    assert calculator.multiplication(-1, 1) == -1
    assert calculator.multiplication(1.5, 1) == 1.5
    assert calculator.multiplication(.5, .5) == .25

def test_division():
    assert calculator.division(10, 2) == 5
    assert calculator.division(10, 1) == 10
    assert calculator.division(-10, 1) == -10
    assert calculator.division(0, 1) == 0
    assert calculator.division(1.5, 1) == 1.5
    assert calculator.division(3, 2) == 1.5
    
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.division(1, 0)
    