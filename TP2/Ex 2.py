from random import randint

dividende = randint(100, 999)
diviseur = randint(2, 9)

est_divisible = dividende % diviseur == 0

reponse = input("Le nombre " + str(dividende) + " est-il divisible par " +
                str(diviseur) + " ? [o/n] ").lower()

if reponse == "o":
    print("Bravo !" if est_divisible else "Perdu !")
elif reponse == "n":
    print("Bravo !" if not est_divisible else "Perdu !")
else:
    print("Réponse incorrecte !")
