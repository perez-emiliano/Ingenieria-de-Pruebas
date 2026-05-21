from calculadora import Calculadora
def test_add():
    calc = Calculadora()
    assert calc.add(2, 3) == 5

def nueva_funcion():
    calc = Calculadora()
    # sustituye `nueva_funcion` y `expected` por los nombres/valores reales
    resultado = calc.mi_nueva_funcion(2, 3)
    assert resultado == 5