if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        dico = {}
        nb_de_mots = 0
        fichier = open(sys.argv[1], "r")
        lignes = fichier.readlines()

        for ligne in lignes:
            ligne = ligne.strip().replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("\"", "") \
                .replace("?", "").replace("!", "")
            for mot in ligne.strip().split():
                nb_de_mots += 1
                if mot not in dico:
                    dico[mot.lower()] = 1
                else:
                    dico[mot.lower()] += 1

        for i, mot in enumerate(sorted(dico, key=dico.get, reverse=True)):
            if i < int(sys.argv[2]):
                print(mot, ":", dico[mot])
        fichier.close()
