from random import randint

amount = int(input("Saisir le nombre de simulations : "))
dices = int(input("Saisir le nombre de dés à utiliser : "))

minimum, maximum = 1 * dices, 6 * dices

results = [0] * (len(range(1, maximum)) + 1)

if amount < 1 or dices < 1:
    print("Erreur de saisie !")
else:

    i = 0
    while i < amount:
        i += 1
        n = randint(minimum, maximum)
        results[n - 1] += 1

    j = minimum
    while j < (6 * dices) + 1:
        print("Coups moyens pour obtenir", j, ":", (results[j - 1] / amount))
        j += 1
