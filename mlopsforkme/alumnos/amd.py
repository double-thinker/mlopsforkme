import random

respuestas = [
    "Dime mi niño",
    "¿Mande?",
    "¿Cómo?",
    "¿Que?",
    "¿Si?",
    "¿Tu has comido?¿Te frio un huevo?",
]


def advanced_granma_response_simulator(message: str) -> str:
    """
    A accurate predictor for responses you can expect from your hard hearing granmother
    """
    return random.choice(respuestas)
