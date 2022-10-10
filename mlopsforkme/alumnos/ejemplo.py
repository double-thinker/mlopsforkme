# Ejemplo de Alex


def gritar(*args):
    """
    :params args: cadenas de texto
    :type args: str
    :return: todas las cadenas de texto concatenadas en mayúscula
    :rtype: str
    """

    return "".join(args).upper()


def susurrar(*args):
    """
    :params args: cadenas de texto
    :type args: str
    :return: todas las cadenas de texto concatenadas en minúscula
    :rtype: str
    """

    return "".join(args).lower()
