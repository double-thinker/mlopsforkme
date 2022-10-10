from mlopsforkme.alumnos.ejemplo import gritar, susurrar


def test_gritar():
    assert gritar("hola", "que", "tal") == "HOLAQUETAL"


def test_susurrar():
    assert gritar("HOLA", "que", "tal") == "holaquetal"
