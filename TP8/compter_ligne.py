

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        fichier = open(sys.argv[1], "r")

        lignes = 0
        mots = 0
        caracteres = 0

        for ligne in fichier:
            lignes += 1
            for mot in ligne.strip().split():
                mots += 1
                caracteres += len(mot) + 1

        fichier.close()
        print(lignes, "lignes,", mots, "mots,", caracteres - 1, "caractères")
