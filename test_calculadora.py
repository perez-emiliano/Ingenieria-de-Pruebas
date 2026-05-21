from calculadora import Calculadora
def test_add():
    calc = Calculadora()
    assert calc.add(2, 3) == 5

def test_nueva_funcion():
    calc = Calculadora()
    assert calc.nueva_funcion(2, 3) == 5