from math import ceil
from random import randint, random

# Définition du rôle joué par l'utilisateur.

role = input("Quel rôle souhaitez-vous incarner ? \n(Alice = Faites deviner le nombre, Bob = Devinez le nombre) ")

if role.lower() == "bob":  # L'utilisateur joue Bob, il doit trouver le nombre.

    # Définition du maximum de l'intervalle de jeu.
    maximum = int(input("Quelle valeur maximum le nombre à deviner ne doit pas dépasser ? "))

    # Génération du nombre à deviner.
    nombre = randint(0, maximum)

    # Initialisation de l'invervalle de jeu.
    b_minimum = 0
    b_maximum = maximum

    # Initialisation du compteur de questions.
    compteur = 0

    # Initialisation du témoin de triche.
    triche = False

    # Calcul du nombre de coups autorisés:
    #
    # Comme le jeu consiste en un enchaînement de dicotomie, donc de division par
    # 2, pour trouver n le maximum de coups autorisés, il faut trouver k la plus
    # petite puissance de 2 tel que 2^k > n.
    coups_restant = 0
    while 2 ** coups_restant <= maximum:
        coups_restant += 1

    # Annonce du nombre de coups autorisés.
    print("Alice : Tu as le droit à", coups_restant, "coup." if coups_restant < 2 else "coups.")

    # BOUCLE PRINCIPALE.
    while True:

        # Régénération du nombre en cas de triche (5% de chance).
        if not triche and random() <= 0.05:
            nombre = randint(0, maximum)
            triche = True

        # Interrogation de l'utilisateur.
        reponse = input("Quelle action souhaitez-vous éxecuter ?\n"
                        "(Q = Poser une question, D = Proposer un nombre, A = Accuser de triche) ")

        if reponse.upper() == "Q":  # L'utilisateur veut poser une question.

            if coups_restant < 1:  # L'utilisateur a utilisé tous ses coups. FIN.
                print("Vous avez utilisé tous vos coups. Perdu !")
                break

            compteur += 1
            question = int(input("Entrez un nombre : "))

            # Affichage de la discution entre l'utilisateur et l'ordinateur.
            print("(Question N°" + str(compteur) + ") Bob : Est-il inférieur à", str(question), "?")

            # Réponse à l'utilisateur et suivi des donnés que ce dernier récolte.
            # Si l'utilisateur trouve avant que l'intervalle de recherche soit
            # assez serré, on affiche un message en fin de partie.
            if question > nombre:
                print("Alice : Oui.")
                b_maximum = question
            else:
                print("Alice : Non.")
                b_minimum = question + 1

            # Décrémentation du compteur de coups restants.
            coups_restant -= 1

        elif reponse.upper() == "D":  # L'utilisateur veut proposer un nombre.

            proposition = int(input("Proposez un nombre : "))

            # Affichage de la discution entre l'utilisateur et l'ordinateur.
            print("Bob : Je propose", str(proposition) + ".")

            if proposition == nombre:  # L'utilisateur gagne la partie. FIN.
                print("Alice : Gagné !")
                if abs(b_maximum - b_minimum) > 1:  # L'utilisateur a gagné sans être certain de trouver le nombre.
                    print("Alice : Tu as eu de la chance !")
            else:  # L'utilisateur perd la partie. FIN.
                print("Alice : Perdu ! C'était", nombre, "!", "J'ai triché ;)")
            break

        elif reponse.upper() == "A":  # L'utilisateur accuse l'ordinateur de tricher. FIN.
            if triche:
                print("Alice : J'admet avoir triché. Bravo, tu gagnes cette partie !")
                break
            else:
                print("Alice : Je n'ai pas triché ! Pour la peine, tu perds cette partie !")
                break

        else:  # L'utilisateur a commis une erreur de saisie.
            print("Erreur de saisie !")

elif role.lower() == "alice":  # L'utilisateur joue Alice, il doit faire deviner un nombre à l'ordinateur.

    # Définition du maximum de l'intervalle de jeu.
    maximum = int(input("Quelle valeur maximum le nombre à deviner ne doit pas dépasser ? "))

    # Initialisation de l'intervalle de jeu.
    b_minimum = 0
    b_maximum = maximum

    # Initialisation du compteur de questions.
    compteur = 0

    # Calcul du nombre de coups autorisés:
    #
    # Comme le jeu consiste en un enchaînement de dicotomie, donc de division par
    # 2, pour trouver n le maximum de coups autorisés, il faut trouver k la plus
    # petite puissance de 2 tel que 2^k > n.
    coups_restant = 0
    while 2 ** coups_restant <= maximum:
        coups_restant += 1

    while True:

        # On effectue une dicotomie en arrondissant au nombre supérieur.
        dicotomie = ceil((b_minimum + b_maximum) / 2)

        print("[DEBUG] Min:", b_minimum, "- Max:", b_maximum)

        compteur += 1

        if coups_restant > coups_restant:  # L'ordinateur à failli à trouver le nombre. FIN.
            print("Bob : Je n'ai pas trouvé.")
            break

        if abs(b_maximum - b_minimum) < 1:  # L'intervalle de recherche est suffisamment serré.

            # Proposition et demande de confirmation à l'utilisateur. FIN.
            proposition = input("Bob : Je propose " + str(b_minimum) + ". Est-ce correct ? ")
            if proposition.lower() == "oui":
                print("Alice : Gagné !")
                break
            elif proposition.lower() == "non":  # L'utilisateur ment, l'ordinateur détecte la triche.
                print("Alice : Per..")
                print("Bob : Un instant ! Tu as triché donc j'ai gagné !")
                break
            else:
                print("Erreur de saisie")
                continue

        # Interrogation de l'ordinateur.
        reponse = input("(Question N°" + str(compteur) + ") Bob : Est-il inférieur à " + str(dicotomie) + " ? ")

        # Mise à jour de l'intervalle de recherche.
        if reponse.lower() == "oui":
            print("Alice : Oui.")
            b_maximum = dicotomie - 1
        elif reponse.lower() == "non":
            print("Alice : Non.")
            b_minimum = dicotomie
        else:
            compteur -= 1
            print("Erreur de saisie !")
            continue

else:  # L'utilisateur a commis une erreur de saisie. FIN.
    print("Erreur de saisie")
