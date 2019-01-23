"""
Test the add() function of the calculator
"""
from calculator import *

def test_add():
    assert add(5,3) == 8

def test_subs():
    assert subs(6,2) == 4
