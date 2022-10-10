from mlopsforkme.alumnos.ejemplo import gritar


def test_gritar():
    assert gritar("NO ", "ME ", "SEAN " "CONFLICTIVOS") == "NO  ME SEAN CONFLICTIVOS"
