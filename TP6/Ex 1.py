from upemtk import *


def cree_polygone():
    """
    Permet de saisir un polygone. Place un point au clic gauche et retourne la liste des points au clic droit.
    :return: (lst) Liste des points du polygone.
    """
    p = []
    while True:
        ev = donne_ev()
        if ev is not None and type_ev(ev) == 'ClicGauche':
            x, y = (abscisse(ev), ordonnee(ev))
            p.append([x, y])
            cercle(x, y, 3, couleur="red")
        elif ev is not None and type_ev(ev) == 'ClicDroit':
            return p
        mise_a_jour()


def dessine_polygone(p):
    """
    Dessine un polygone à partir d'une liste de points.
    :param p: (lst) Liste des coordonées.
    """
    efface_tout()
    i = 0
    while i < len(p):
        if i == len(p) - 1:
            ligne(p[i][0], p[i][1], p[0][0], p[0][1])
        else:
            ligne(p[i][0], p[i][1], p[i + 1][0], p[i + 1][1])
        i += 1


cree_fenetre(600, 600)

points = cree_polygone()

if len(points) > 0:

    x1, y1 = points[0]
    x2, y2 = points[0]
    i = 0
    while i < len(points):
        x, y = points[i]
        if x < x1:
            x1 = x
        if x > x2:
            x2 = x
        if y < y1:
            y1 = y
        if y > y2:
            y2 = y
        i += 1

    dessine_polygone(points)
    rectangle(x1, y1, x2, y2, couleur="gray")

attend_fermeture()
