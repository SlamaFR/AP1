n = int(input("Hauteur du triangle : "))

i = 0
while i < n:
    i += 1
    print(i * "*")

n = int(input("Hauteur de la ligne : "))

i = 0
while i < n:
    i += 1
    print((n - i) * " " + "*")

n = int(input("Hauteur de la pyramide : "))

i = 0
while i < n:
    i += 1
    print((n - i) * " " + (2 * i - 1) * "*")
