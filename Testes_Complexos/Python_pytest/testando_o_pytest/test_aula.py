import pytest
from Sendo_testados import *

def test_soma_1():
    assert soma_1(41) == 42


def test_soma_1_numero_como_string():
    assert soma_1('41') == 42

def test_soma_1_palavra():
    with pytest.raises(ValueError):
        soma_1('fabio')

# def test_x():
#     with pytest.raises(ValueError):
#         soma_1(10)