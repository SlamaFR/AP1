def maj_dico_liste(dico, cle, element):
    """
    Ajoute l'élément dans la liste du dico correspondant à la clé.
    :param dico: Dictionnaire.
    :param cle: Clé.
    :param element: Élement à ajouter.
    """
    if cle not in dico:
        dico[cle] = [element]
    else:
        dico[cle].append(element)


def creer_dico_prenoms():
    """
    Créer un dictionnaire des prénoms contenus dans le fichier 'prenoms.csv'.
    :return dict: Dictionnaire créé.
    """
    dico = {}
    fichier = open("prenoms.csv", "r")

    for i, ligne in enumerate(fichier):
        if i == 0:
            continue
        cases = ligne.strip().split(";")
        for langue in cases[2].split(", "):
            maj_dico_liste(dico, langue, cases[0])
    fichier.close()
    return dico


def affiche_prenoms(nom_fichier, prenoms):
    """
    Affiche les prénoms de la liste qui sont dans le fichier.
    :param str nom_fichier: Nom du fichier.
    :param list prenoms: Liste de prénoms.
    """
    fichier = open(nom_fichier, "r")
    for ligne in fichier:
        for mot in ligne.strip().split():
            mot = mot.replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("\"", "") \
                .replace("?", "").replace("!", "")
            if mot in prenoms:
                print(mot)
    fichier.close()


def affiche_prenoms_stats(nom_fichier, prenoms, destination):
    fichier = open(nom_fichier, "r")
    sortie = open(destination, "w")
    dico = {}
    for ligne in fichier:
        for mot in ligne.strip().split():
            mot = mot.replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("\"", "") \
                .replace("?", "").replace("!", "")
            if mot in prenoms:
                if mot in dico:
                    dico[mot] += 1
                else:
                    dico[mot] = 1
    for cle in sorted(dico, key=dico.get, reverse=True):
        sortie.write(cle + " : " + str(dico[cle]) + " fois\n")
    fichier.close()
    sortie.close()


prenoms = creer_dico_prenoms()
print(prenoms["french"])
print(prenoms["russian"])
french_and_russian = []
for prenom in prenoms["russian"]:
    if prenom in prenoms["french"]:
        french_and_russian.append(prenom)
print(french_and_russian)

affiche_prenoms_stats("sense_and_sensibility.txt", prenoms["english"], "resultat.txt")
