N_input = int(input("Saisir un entier naturel :"))

if N_input < 0:
    print("Erreur de saisie !")
else:
    i = 0
    while i < N_input:
        i += 1
        print("Et", i, "moutons" if i > 1 else "mouton")
    print("Bonne nuit...")
