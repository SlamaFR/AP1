# auteurs/mails		:  C. Pivoteau - pivoteau@univ-mlv.fr
#					   A. Meyer
# date de création	: 2015
# modifs            : 2018
# description		: programme pour découvrir upemtk

from random import randrange
from time import sleep

from upemtk import *

#### debut de partie a modifier ####

t = int(input("Saisir la taille de la fenêtre : "))  # Dimension de la fenêtre.
n = int(input("Saisir le nombre de figure à dessiner : "))  # Nombre de figures à dessiner.
dr = False  # Figure à dessiner (True = rectangle, False = cercle)
p = float(input("Saisir le délair entre deux dessins : "))  # Délai entre deux dessins.

c0 = "red"  # Couleur du texte initial.
c1 = "purple"  # Couleur du contour des carrés.
c2 = "black"  # Couleur du contour des cercles.
c3 = ""  # Couleur de l'intérieur des carrés.
c4 = "pink"  # Couleur de l'intérieur des cercles.

#### fin de partie a modifier ####


### NE PAS MODIFIER CE QUI SUIT


if type(t) != type(int()):
    print('La valeur de t doit etre entiere, ', t, " n'est pas correct!")
    quit()
if t > 1000:
    print("La valeur de t est trop grande.")
    quit()
if t < 100:
    print("La valeur de t est trop petite.")
    quit()

if type(n) != type(int()):
    print('La valeur de n doit etre entiere, ', n, " n'est pas correct!")
    quit()
if n > 1000:
    print("La valeur de n est trop grande.")
    quit()
if n < 1:
    print("La valeur de n est trop petite.")
    quit()

if type(dr) != type(True):
    print('dr est un booleen!')
    quit()

if type(p) != type(0.1):
    print('La valeur de p doit etre decimale, ', p, " n'est pas correct!")
    quit()
if p > 2.0:
    print("La valeur de p est trop grande.")
    quit()
if p < 0.0:
    print("La valeur de p est trop petite.")
    quit()


def test_couleurs(c):
    if not c in {"", "black", "blue", "red", "green", "yellow", "pink", "purple", "orange"}:
        print(c + " n'est pas une couleur.")
        quit()


test_couleurs(c0)
test_couleurs(c1)
test_couleurs(c2)
test_couleurs(c3)
test_couleurs(c4)


def rectangle_aleatoire(x, y, temps):
    rectangle(x, y, x + temps, y + temps, c1, c3)


def cercle_aleatoire(x, y, temps):
    cercle(x, y, temps / 2, c2, c4)


def ready():
    texte(t / 2, t / 2, "Tapez sur une touche !", c0, "center")
    attend_ev()
    efface_tout()


cree_fenetre(t, t)
ready()

temps = 1

while temps != n:
    # geler le programme pendant p secondes
    sleep(p)

    # attente d'un événement
    ev = donne_ev()
    typeEv = type_ev(ev)
    if typeEv == "ClicGauche":
        dr = not dr
    elif typeEv == "Quitte":
        break

    # tirage aléatoire de deux entiers entre 0 et t-1
    x, y = randrange(0, t), randrange(0, t)
    if dr:
        rectangle_aleatoire(x, y, temps)
    else:
        cercle_aleatoire(x, y, temps)
    temps = temps + 1

    mise_a_jour()

attend_ev()
ferme_fenetre()
