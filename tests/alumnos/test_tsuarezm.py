from mlopsforkme.alumnos.tanasuarez import suma

def test_suma_positivos():
    """
    este teest comprueba la suma de dos numeros positivos
    """
    assert suma(2,2) == 4

def test_suma_distintos():
    """
    este teest comprueba la suma de dos numeros distintos
    """
    assert suma(2,-2) == 0