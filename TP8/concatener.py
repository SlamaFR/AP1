if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        resultat = ""
        for i in range(len(sys.argv) - 1):
            fichier = open(sys.argv[i + 1], "r")
            resultat += fichier.read()
            fichier.close()
        print(resultat)
