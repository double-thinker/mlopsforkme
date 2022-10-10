from mlopsforkme.alumnos.juanse77 import suma


def test_suma_positivo():
    assert suma(2, 3) == 5


def test_suma_negativo_uno():
    assert suma(2, -3) == -1
    assert suma(-2, 3) == 1


def test_suma_negativo_dos():
    assert suma(-3, -2) == -5
