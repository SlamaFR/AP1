from doctest import testmod


def compter(nom_fichier):
    """
    Compte le nombre de lignes, de mots et de caractères dans le fichier donné.
    :param str nom_fichier: Nom du fichier
    :return tuple: Nombre de lignes, mots et caractères.

    >>> compter("doctest.txt")
    (3, 6, 11)
    """
    fichier = open(nom_fichier, "r")

    lignes = 0
    mots = 0
    caracteres = 0

    for ligne in fichier:
        lignes += 1
        for mot in ligne.strip().split():
            mots += 1
            caracteres += len(mot) + 1

    fichier.close()
    return lignes, mots, caracteres - 1


def liste_mots(nom_fichier):
    """
    Retourne une liste des mots contenus dans le fichier.
    :param str nom_fichier: Nom du fichier.
    :return list: Liste des mots du fichier.

    >>> liste_mots("doctest.txt")
    ['a', 'a', 'b', 'a', 'b', 'c']
    """
    fichier = open(nom_fichier, "r")
    mots = []

    for ligne in fichier:
        for mot in ligne.strip().split():
            mots.append(mot)

    fichier.close()
    return mots


def recopier(entree, sortie):
    """
    Recopie le contenu du premier fichier dans le deuxième.
    :param str entree: Nom du fichier de départ.
    :param str sortie: Nom du fichier de destination.
    """
    depart = open(entree, "r")
    destination = open(sortie, "w")

    for ligne in depart:
        destination.write(ligne)

    depart.close()
    destination.close()


def substituer(entree, avant, apres, sortie):
    """
    Recopie le contenu du fichier de départ vers le fichier de destination en remplaçant
    la chaîne avant par la chaîne après.
    :param str entree: Nom du fichier de départ.
    :param str avant: Chaîne à remplacer.
    :param str apres: Chaîne de remplacement.
    :param str sortie: Nom du fichier de destination.
    """
    depart = open(entree, "r")
    destination = open(sortie, "w")

    for ligne in depart:
        destination.write(ligne.replace(avant, apres))

    depart.close()
    destination.close()


testmod()
