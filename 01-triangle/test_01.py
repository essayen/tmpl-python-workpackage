import pytest
import ex_01

def test_01_hyp():
    assert ex_01.triangle_hyp(3.0,4.0) == 5.0

def test_01_area():
    assert ex_01.triangle_area(3.0,4.0) == 6.0

def test_01_circ():
    assert ex_01.triangle_circ(3.0,4.0) == 12.0