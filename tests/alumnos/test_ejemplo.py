from mlopsforkme.alumnos.ejemplo import gritar


def test_gritar():
    # Nos quedamos los dos asserts. El de abel y el mio
    assert gritar("hola", "que") == "HOLAQUE"
    assert gritar("hola", "que", "talestas") == "HOLAQUETALESTAS"
