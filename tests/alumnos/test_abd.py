from mlopsforkme.alumnos.abd import camelCase


def test_camelCase():
    assert camelCase("hey", "listen") == "HeyListen"
