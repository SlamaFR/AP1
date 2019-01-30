from turtle import *
import doctest
import math


def triangle(d1, a, d2):
    """
    Cette fonction dessine un triangle.
    :param d1: (int ou float) Première longueur.
    :param a: (int ou float) Angle.
    :param d2: (int ou float) Deuxième longueur.
    :returns Périmètre du triangle.

    >>> triangle(30, 90, 40)
    120.0
    """
    if a >= 180:
        return 0
    else:
        reset()
        fd(d1)
        left(180 - a)
        fd(d2)
        x, y = xcor(), ycor()
        d3 = round(math.sqrt(x ** 2 + y ** 2), 1)
        goto(0, 0)
        return d1 + d2 + d3


def triangle_isocele(d1, a):
    """
    Cette fonction dessine un triangle isocèle.
    :param d1: (int ou float) Longueur des deux côtés égaux.
    :param a: (int ou float) Angle.
    :returns Périmètre du triangle.

    >>> triangle_isocele(60, 60)
    180.0
    """
    if a >= 180:
        return 0
    else:
        return triangle(d1, a, d1)


def triangle_equilateral(d1):
    """
    Cette fonction dessine un triangle équilatéral.
    :param d1: (int ou float) Longueur des côtés.
    :returns Périmètre du triangle.

    >>> triangle_equilateral(40)
    120.0
    """
    return triangle(d1, 60, d1)


def quadrilatere(d1, a1, d2, a2, d3):
    """
    Cette fonction dessine un quadrilatère quelconque.
    :returns Périmètre du quadrilatère.
    >>> quadrilatere(100, 100, 200, 80, 100)
    600.0
    """
    reset()
    fd(d1)
    left(a1)
    fd(d2)
    left(a2)
    fd(d3)
    x, y = xcor(), ycor()
    d4 = math.sqrt(x ** 2 + y ** 2)
    goto(0, 0)
    return d1 + d2 + d3 + d4


def rectangle(d1, d2):
    """
    Cette fonction dessine un rectangle.
    :param d1: (int ou float) Longueur.
    :param d2: (int ou float) Largeur.
    :returns Périmètre du rectangle.

    >>> rectangle(200, 300)
    1000.0
    """
    return quadrilatere(d1, 90, d2, 90, d1)


def parallelogramme(d1, a, d2):
    """
    Cette fonction dessine un parallélogramme.
    :param d1: (int ou float) Longueur.
    :param a: (int ou float) Premier angle.
    :param d2: (int ou float) Largeur.
    :returns Périmètre du parallélogramme.

    >>> parallelogramme(200, 40, 300)
    1000.0
    """
    return quadrilatere(d1, a, d2, 180 - a, d1)


def losange(d1, a):
    """
    Cette fonction dessine un losange.
    :param d1: (int ou float) Longueur.
    :param a: (int ou float) Angle.
    :returns Périmètre du rectangle.

    >>> losange(60, 40)
    240.0
    """
    return parallelogramme(d1, a, d1)


def carre(d1):
    """
    Cette fonction dessine un carré.
    :param d1: (int ou float) Longueur.
    :returns Périmètre du carré.

    >>> carre(200)
    800.0
    """
    return rectangle(d1, d1)


def polygone(d1, n):
    """
    Cette fonction dessine un polygône à n côtés.
    :param d1: (int ou float) Longueur.
    :param n: (int) Nombre de côtés.
    :returns Périmètre du polygône.

    >>> polygone(50, 6)
    300
    """
    reset()
    a = (n - 2) * 180 / n
    i = 0
    while i < n:
        i += 1
        fd(d1)
        left(180 - a)
    return n * d1


doctest.testmod()

exitonclick()
