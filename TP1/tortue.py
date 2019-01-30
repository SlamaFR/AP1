from turtle import *

#### debut de partie a modifier ####

nbLignes = int(input("Saisir le nombre de côtes du polygône :"))

lgLigne = int(input("Saisir la longueur des côtés du polygône : "))

angle = 360 / nbLignes

xInit = -lgLigne / 2

yInit = -lgLigne / 2

#### fin de partie a modifier ####


### Ne pas modifier ce qui suit ###
reset()
up()
goto(xInit, yInit)
down()
a = 0
while a < nbLignes:
    a += 1
    forward(lgLigne)
    left(angle)

exitonclick()
