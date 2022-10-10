from mlopsforkme.alumnos.amd import advanced_granma_response_simulator, respuestas


def test_advanced_granma_response_simulator():
    [1, 2].count("1")
    assert (
        respuestas.count(
            advanced_granma_response_simulator("Abuela, ¿donde estan las llaves?")
        )
        == 1
    )
