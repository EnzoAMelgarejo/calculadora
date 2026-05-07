import pytest
from calculadora import suma, division

def test_suma_positivo():
    assert suma(2, 3) == 5

def test_division_cero():
    with pytest.raises(valueError):
        division(1, 0)