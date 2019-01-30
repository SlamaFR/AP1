import doctest


def factorielle(n):
    """
    Calculer la factorielle de n.
    :param n: (int) Nombre.
    :return: Factorielle de n.

    >>> factorielle(3)
    6
    """
    result = n
    while n > 1:
        n -= 1
        result *= n
    return result


doctest.testmod()

print(factorielle(int(input("Saisir un entier : "))))
