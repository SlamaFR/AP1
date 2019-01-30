from upemtk import *

# création de la fenêtre graphique
cree_fenetre(600, 600)

# sélection des coins et dessin du premier rectangle
x1, y1 = attend_clic_gauche()
x2, y2 = attend_clic_gauche()
rectangle(x1, y1, x2, y2, couleur='blue', epaisseur=3)

# sélection des coins et dessin du second rectangle
x3, y3 = attend_clic_gauche()
x4, y4 = attend_clic_gauche()
rectangle(x3, y3, x4, y4, couleur='red', epaisseur=3)

# partie à compléter
if x1 > x2:
    x1, x2 = x2, x1

if y1 > y2:
    y1, y2 = y2, y1

if x3 > x4:
    x3, x4 = x4, x3

if y3 > y4:
    y3, y4 = y4, y3

disjoints = not (((x1 <= x3 <= x2 or x1 <= x4 <= x2) and (y3 <= y1 <= y4 or y3 <= y2 <= y4)) or
                 ((x3 <= x1 <= x4 or x3 <= x2 <= x4) and (y1 <= y3 <= y2 or y1 <= y4 <= y2)))

rouge_entierement_dans_bleu = (x1 <= x3 <= x2 and x1 <= x4 <= x2 and y1 <= y3 <= y2 and y1 <= y4 <= y2)

bleu_entierement_dans_rouge = (x3 <= x1 <= x4 and x3 <= x2 <= x4 and y3 <= y1 <= y4 and y3 <= y2 <= y4)

if rouge_entierement_dans_bleu or bleu_entierement_dans_rouge:
    texte(300, 300, "Recouvrement total", taille=24, ancrage="center")
    texte(300, 300, "Disjoints", taille=24, ancrage="center")
else:
    texte(300, 300, "Recouvrement partiel", taille=24, ancrage="center")

# fermeture de la fenêtre
attend_fermeture()
