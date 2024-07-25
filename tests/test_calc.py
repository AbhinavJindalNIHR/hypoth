import pytest
import hypoth.source as sc
# test sqrt function
def test_sqrt():
    input = 4
    e_output = 2.0
    output = sc.sqrt(input)
    assert output == e_output
# test hypoth function

def test_sqrt_even():
    input = 36
    e_output = 6
    output = sc.sqrt(input)
    assert output == e_output
    
def test_sqrt_negative():
    input = -9
    e_output = 3
    output = sc.sqrt(input)
    assert output == e_output
    
    