from upemtk import *
import math

COULEURS = ['black', 'snow', 'navy', 'dark green', 'deep pink', 'brown1', 'gold2', 'red', 'yellow', 'purple2', 'green3', 'pink', 'orange', 'magenta', 'lime', 'purple', 'blue2', 'white', 'gold']


def affiche_triangle(taille, p):
    """
    Affiche un triangle de Pascal modulo p.
    :param taille: (int) Taille du triangle strictement positive.
    :param p: (int) Modulo p.
    """

    pair = [0] * taille
    impair = [0] * taille
    pair[0] = 1
    impair[0], impair[1] = 1, 1

    y = 0
    while y < taille:
        x = 0
        if y % 2 == 0:  # Pair
            while x < y + 1:
                pair[x] = (impair[x - 1] % p + impair[x] % p) % p
                point(x, y, COULEURS[pair[x]])
                x += 1
        else:  # Impair
            while x < y + 1:
                impair[x] = (pair[x - 1] % p + pair[x] % p) % p
                point(x, y, COULEURS[impair[x]])
                x += 1
        y += 1


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


taille = int(input("Saisir la taille de la fenêtre : "))
cree_fenetre(taille, taille)

p = 2
while p <= 19:
    if not est_premier(p):
        p += 1
        continue
    affiche_triangle(taille, p)
    print("Modulo =", p)
    attend_clic_gauche()
    p += 1

attend_fermeture()
