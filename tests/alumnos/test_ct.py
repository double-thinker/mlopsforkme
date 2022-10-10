from mlopsforkme.alumnos.ct import imprimir_nombre


def test_imprimir_nombre():
    assert imprimir_nombre("Cristian") == "Me llamo Cristian"
