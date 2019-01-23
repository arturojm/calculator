"""
Test the add() function of the calculator
"""
from calculator import *

def test_add():
    assert add(5,3) == 8

def test_no_parameters():
    assert add() == 0

def test_mult_parameters():
    assert add(4,5,6,10) == 25

def test_subs():
    assert subs(6,2) == 4
