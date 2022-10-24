from mlopsforkme.alumnos.ejemplo import gritar


def test_gritar():
    assert gritar("NO ", "ME ", "SEAN " "CONFLICTIVOS") == "NO ME SEAN CONFLICTIVOS"
    # Nos quedamos los dos asserts. El de abel y el mio
    assert gritar("hola", "que") == "HOLAQUE"
    assert gritar("hola", "que", "talestas") == "HOLAQUETALESTAS"
