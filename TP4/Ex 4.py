import doctest
import math


def est_premier(n):
    """
    Détermine si n est un nombre premier.
    :param n: (int) Nombre n.
    :return: (bool) Résultat.

    >>> est_premier(3)
    True
    """
    i = 1
    while i < math.sqrt(n):
        i += 1
        if n % i == 0:
            if i == n:
                return True
            else:
                return False
    return True


def premier_suivant(n):
    """
    Détermine le premier nombre entier supérieur à n.
    :param n: (int) Nomnbre n.
    :return: (int) Nombre entier supérieur à n

    >>> premier_suivant(2)
    3
    """
    while True:
        n += 1
        if est_premier(n):
            return n


def affiche_premiers(n):
    """
    Affiche tous les nombres premiers inférieurs à n
    :param n: (int) Nombre n.

    >>> affiche_premiers(5)
    2
    3
    """
    i = 2
    while i < n:
        if est_premier(i):
            print(i)
        i += 1


def contient_puissance(n, p):
    """
    Calcule la plus grande puissance de p tel que n soit divisible par celle-ci.
    :param n: (int) Nombre.
    :param p: (int) Nombre premier.
    :return: (int) Puissance de p.

    >>> contient_puissance(1024, 2)
    10
    """
    if not est_premier(p):
        return
    i = 0
    while n % p == 0:
        i += 1
        n //= p
    return i


def decomposition(n):
    """
    Décomposer l'entier n comme le produit de puissances de nombres premiers.
    :param n: (int) Nombre.
    :return: (str) Expression de la décomposition.

    >>> decomposition(301158)
    '301158 = 2**1 * 3**4 * 11**1 * 13**2'
    """
    i = 0
    quotient = n
    p = 2
    result = str(n) + " = "
    while quotient != 1:
        power = contient_puissance(quotient, p)
        if power < 1:
            p = premier_suivant(p)
            continue

        quotient = quotient // p ** power
        if i > 0:
            result += " * "
        result += str(p) + "**" + str(power)
        p = premier_suivant(p)
        i += 1
    return result


doctest.testmod()
