import doctest


def valeur_approchee(f):
    """
    Donne une valeur approchée de la fraction f
    à quatre chiffres après la virgule.
    :param f: (tuple) Fraction.
    :return: (float) Valeur approchée de la fraction f.

    >>> valeur_approchee((4, 3))
    1.3333
    """
    (a, b) = f
    return round(a / b, 4)


def simplifier(f):
    """
    Simplifie la fraction f.
    :param f: (tuple) Fraction.
    :return: (tuple) Fraction simplifiée.

    >>> simplifier((2, 4))
    (1, 2)
    """

    (a, b) = f
    pgcd = abs(b)

    while a % pgcd != 0 or b % pgcd != 0:
        pgcd -= 1

    return a // pgcd, b // pgcd


def oppose(f):
    """
    Donne l'opposé de la fraction f.
    :param f: (tuple) Fraction.
    :return: (tuple) Fraction opposée.

    >>> oppose((1, 3))
    (-1, 3)
    """
    (a, b) = f
    return simplifier((-a, b))


def inverse(f):
    """
    Donne l'inverse de la fraction f.
    :param f: (tuple) Fraction.
    :return: (tuple) Fraction inversée.

    >>> inverse((6, 12))
    (2, 1)
    """
    (a, b) = f
    return simplifier((b, a))


def multiplier(f, g):
    """
    Multiplier deux fractions entre elles.
    :param f: (tuple) Permière fraction.
    :param g: (tuple) Deuxième fraction.
    :return: (tuple) Produit des fractions.

    >>> multiplier((1, 4), (1, 2))
    (1, 8)

    """
    (a, b) = f
    (c, d) = g
    return simplifier((a * c, b * d))


def diviser(f, g):
    """
    Diviser deux fractions entre elles.
    :param f: (tuple) Permière fraction.
    :param g: (tuple) Deuxième fraction.
    :return: (tuple) Quotient des fractions.

    >>> diviser((1, 4), (1, 2))
    (1, 2)

    """
    (a, b) = f
    (c, d) = inverse(g)
    return simplifier((a * c, b * d))


def additionner(f, g):
    """
    Additionner deux fractrion.
    :param f: (tuple) Première fraction.
    :param g: (tuple) Deuxième fraction.
    :return: (tuple) Somme des fractions.

    >>> additionner((1, 4), (1, 2))
    (3, 4)
    """
    (a, b) = f
    (c, d) = g

    return simplifier((a * d + c * b, b * d))


def soustraire(f, g):
    """
    Soustraire deux fractrion.
    :param f: (tuple) Première fraction.
    :param g: (tuple) Deuxième fraction.
    :return: (tuple) Différence des fractions.

    >>> soustraire((1, 2), (1, 4))
    (1, 4)
    """
    return additionner(f, oppose(g))


doctest.testmod()
