from upemtk import *

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        image = open(sys.argv[1], "r")

        lignes = image.readlines()

        x, y = int(lignes[1]), int(lignes[2])
        valeur_max = int(lignes[3])

        cree_fenetre(x + 5, y + 5)

        for i, ligne in enumerate(lignes):
            if i > 3:
                values = ligne.strip().split()
                j = 0
                while j < len(values):
                    pixel = int(values[j]), int(values[j + 1]), int(values[j + 2])
                    rectangle(j // 3, i, j // 3, i, couleur="#" + "%0.2X" % (pixel[0] * 255 // valeur_max) + "%0.2X" % (
                            pixel[1] * 255 // valeur_max) + "%0.2X" % (pixel[2] * 255 // valeur_max))
                    j += 3

        attend_fermeture()
