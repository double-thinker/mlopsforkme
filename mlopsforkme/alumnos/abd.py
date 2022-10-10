# Ejemplo de Abel


def camelCase(*args):
    return "".join(["".join([a[0].upper(), a[1:]]) for a in args])
