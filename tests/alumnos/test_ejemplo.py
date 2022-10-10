from mlopsforkme.alumnos.ejemplo import gritar


def test_gritar():
    assert gritar("hola", "que", "tal") == "HOLAQUETAL"
