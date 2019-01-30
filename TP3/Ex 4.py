continue_asking = True

somme = 0
count = 0
precedent = 0

i = 0
while continue_asking:
    i += 1
    n = int(input("Entier N°" + str(i) + " : "))
    if n == 0:
        continue_asking = False
        break

    if i == 1 or n > precedent:
        precedent = n
        somme += n
        count += 1

print("Nombre d'éléments :", count, "Somme :", somme)
