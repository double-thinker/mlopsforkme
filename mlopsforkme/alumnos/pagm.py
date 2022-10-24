# Función que suma cualquier número de valores numéricos.
# Entrada números.
# Salida La suma de todos los números recibidos ajusando el tipo."""


def suma_n(*numeros):
    """
    Esta función suma n números

    Parámetros
    ----------

    :param *numeros: operandos
    :type *numeros: int, float, complex

    :raises: si los números no se pueden sumar

    :return: suma de todos los números
    :rtype: int, float, complex

    Ejemplos
    --------

    >>> from mlopsforkme.alumnos.pagm import suma_n
    >>> suma_n(5,5,5,5,5,5,5,5,5, 23.12, complex(3,4))
    (71.12+4j)

    """

    suma = 0

    for numero in numeros:
        suma = suma + numero

    return suma
