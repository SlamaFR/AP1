from doctest import testmod


def maj_dico_compte(dico: dict, mot: str):
    """
    Incrémente la valeur correspondant au mot dans le dictionnaire donné.
    :param dico: Dictionnaire.
    :param mot: Clé à incrémenter.
    """
    if mot not in dico:
        dico[mot] = 1
    else:
        dico[mot] += 1


def compte_mots(chaine: str):
    """
    Compte les occurences de chaques mots dans la chaîne de caractères.
    :param srt chaine: Chaîne de caractère.
    :return dict: Dictionnaire contenant les occurences de chaque mot.

    >>> compte_mots("Bonjour je suis grand et je suis beau")
    {'Bonjour': 1, 'je': 2, 'suis': 2, 'grand': 1, 'et': 1, 'beau': 1}
    """
    resultat = {}
    for mot in chaine.split():
        maj_dico_compte(resultat, mot)
    return resultat


def compte_mot_total(dico: dict):
    """
    Compte le nombre total d'occurence de chaque mot du dictionnaire.
    :param dict dico: Dictionnaire.
    :return int: Nombre total d'occurences.

    >>> compte_mot_total({'Bonjour': 1, 'je': 2, 'suis': 2, 'grand': 1, 'et': 1, 'beau': 1})
    8
    """
    resultat = 0
    for mot in dico:
        resultat += dico[mot]
    return resultat


def affiche_mots(entree: str):
    """
    Affiche de nombre de mots total, de mots différents et le nombre
    d'occurences de chaque nombre.
    :param entree: Fichier source.

    >>> affiche_mots("doctest.txt")
    Nombre de mots : 6 - Nombre de mots différents : 3
    a : 3
    b : 2
    c : 1
    """
    dico = {}
    nb_de_mots = 0
    fichier = open(entree, "r")
    lignes = fichier.readlines()

    for ligne in lignes:
        ligne = ligne.strip().replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("\"", "") \
            .replace("?", "").replace("!", "")
        for mot in ligne.strip().split():
            nb_de_mots += 1
            maj_dico_compte(dico, mot.lower())

    print("Nombre de mots :", nb_de_mots, "- Nombre de mots différents :", len(dico))
    for mot in dico:
        print(mot, ":", dico[mot])


def affiche_mots_importants(entree: str):
    """
    Affiche les mots donc le nombre d'occurences représentent entre 0.02%
    et 0.2% du fichier.
    :param entree: Fichier source.
    """
    dico = {}
    nb_de_mots = 0
    fichier = open(entree, "r")
    lignes = fichier.readlines()

    for ligne in lignes:
        ligne = ligne.strip().replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("\"", "") \
            .replace("?", "").replace("!", "")
        for mot in ligne.strip().split():
            nb_de_mots += 1
            maj_dico_compte(dico, mot.lower())

    for mot in sorted(dico, key=dico.get):
        if 0.02 <= dico[mot] / nb_de_mots <= 0.2:
            print(mot, ":", dico[mot])


un_dico = {'toto': 3, 'titi': 1, 'tutu': 42}

un_dico['tata'] = 8
un_dico['titi'] += 1

testmod()

affiche_mots_importants("sense_and_sensibility.txt")
