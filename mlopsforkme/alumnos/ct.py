# funcion random


def imprimir_nombre(nombre: str) -> str:
    """Imprime el nombre

    :param nombre: nombre del usuario
    :type nombre: str
    :return: nombre del usuario
    :rtype: str

    >>> from mlopsforkme.alumnos.ct import imprimir_nombre
    >>> imprimir_nombre("Menganito")
    'Me llamo Menganito'
    """
    return f"Me llamo {nombre}"
