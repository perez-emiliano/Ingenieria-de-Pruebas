from calculadora import Calculadora
def test_add():
    calc = Calculadora()
    assert calc.add(2, 3) == 5