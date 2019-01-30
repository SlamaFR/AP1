from upemtk import *

COULEURS = ['white', 'red']


def init(n):
    """
    Génère une liste de listes de longueurs n
    :param n: (int) Longueur des listes.
    :return: (lst) Liste contenant les lignes du plateau.

    >>> init(2)
    [[0, 0], [0, 0]]
    """
    result = []
    i = 0
    while i < n:
        result.append([0] * n)
        i += 1
    return result


def dessine_plateau(plateau, mise_a_jour):
    """
    Dessine un plateau à partir d'une liste de liste.
    :param plateau: (lst) Liste contenant des listes de plateau.
    :param mise_a_jour: (bool) Détermine si le plateau doit se mettre à jour.
    """
    index = 0
    y = 0
    while y < len(plateau):
        x = 0
        while x < len(plateau[y]):
            if plateau[y][x] == 0:
                if mise_a_jour:
                    efface(index)
                rectangle(x * 100, y * 100, x * 100 + 100, y * 100 + 100, tag=str(index), remplissage='white')
            else:
                if mise_a_jour:
                    efface(index)
                rectangle(x * 100, y * 100, x * 100 + 100, y * 100 + 100, tag=str(index), remplissage='red')
            index += 1
            x += 1
        y += 1


def clique_case(x_case, y_case, plateau):
    """
    Intervertit les états de la case cliquée et des ses voisines.
    :param x_case: (int) Abscisse de la case cliquée.
    :param y_case: (int) Ordonnée de la case cliquée.
    :param plateau: (lst) Plateau.
    """
    plateau[y_case][x_case] = abs(plateau[y_case][x_case] - 1)
    if y_case - 1 >= 0:
        plateau[y_case - 1][x_case] = abs(plateau[y_case - 1][x_case] - 1)
    if y_case + 1 <= taille_plateau - 1:
        plateau[y_case + 1][x_case] = abs(plateau[y_case + 1][x_case] - 1)
    if x_case - 1 >= 0:
        plateau[y_case][x_case - 1] = abs(plateau[y_case][x_case - 1] - 1)
    if x_case + 1 <= taille_plateau - 1:
        plateau[y_case][x_case + 1] = abs(plateau[y_case][x_case + 1] - 1)


def verifier_victoire(plateau):
    """
    Vérifie si toutes les cases du plateau sont "alumées" et
    retourne un booléen déterminant si le joueur a gagné.
    :param plateau: (lst) Plateau.
    :return: (bool) Continuer le jeu.

    >>> verifier_victoire([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    True
    """
    i = 0
    while i < len(plateau):
        if 0 not in plateau[i]:
            if i < len(plateau) - 1:
                i += 1
            else:
                return True
        else:
            return False


taille_plateau = 5
plateau = init(taille_plateau)
cree_fenetre(len(plateau) * 100, len(plateau) * 100)
dessine_plateau(plateau, False)

jouer = True
while jouer:

    x, y = attend_clic_gauche()
    x_case = x // 100
    y_case = y // 100

    clique_case(x_case, y_case, plateau)
    dessine_plateau(plateau, True)
    jouer = not verifier_victoire(plateau)

    mise_a_jour()

texte(len(plateau) * 100 / 2, len(plateau) * 100 / 2, " Victoire ! ", couleur='white', ancrage='center', taille=32)

attend_fermeture()
