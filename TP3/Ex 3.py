continue_asking = True

maximum, minimum = 0, 0

i = 0
while continue_asking:
    i += 1
    n = int(input("Entier N°" + str(i) + " : "))
    if i == 1:
        minimum = n
        maximum = n
    if n < 0:
        continue_asking = False
    if n > maximum:
        maximum = n
    if n < minimum:
        minimum = n

if i < 2:
    print("La liste d'entiers saisie est vide !")
else:
    print("Minimum :", minimum)
    print("Maximum :", maximum)
