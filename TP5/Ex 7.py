from math import sqrt
from random import randint

from matplotlib import pyplot


def jet_des(k, p):
    """
    Simule un lancer de k dés à n faces.
    :param k: (int) Nombre de dés.
    :param p: (int) Nombre de faces.
    :return: (int) Résultat du lancer.

    >>> jet_des(2, 6)
    """
    result = 0
    i = 0
    while i < k:
        result += randint(1, p)
        i += 1
    return result


def histogramme(n, k, p):
    """
    Retourne un tableau des occurences des valeurs de n lancers de k dés à p faces.
    :param n: (int) Nombre de lancers.
    :param k: (int) Nombre de dés.
    :param p: (int) Nombre de faces.
    :return: (list) Occurences de chaque valeurs.

    >>> graphique(10000, 10, 6)
    """
    i = 0
    result = [0] * ((k * p) - k + 1)
    while i < n:
        toss = jet_des(k, p)
        result[toss - k] += 1
        i += 1
    return result


def graphique(n, k, p):
    """
    Trace un graphique de répartition de n tirages de k dés à n faces.
    :param n: (int) Nombre de lancers.
    :param k: (int) Nombre de dés.
    :param p: (int) Nombre de faces.
    :return: (float) Écart-type.


    >>> graphique(10000, 10, 6)
    """
    ordonnees = histogramme(n, k, p)
    abscisses = [0] * ((k * p) - k + 1)

    i = 0
    j = k
    while i < ((k * p) - k + 1):
        abscisses[i] = j
        j += 1
        i += 1

    average = 0
    i = 0
    while i < len(ordonnees):
        average += ordonnees[i] * abscisses[i]
        i += 1
    average /= n

    sigma = 0
    i = 0
    while i < len(ordonnees):
        sigma += ordonnees[i] * (average - abscisses[i]) ** 2
        i += 1
    sigma = sqrt(sigma / n)

    pyplot.bar(abscisses, ordonnees)
    pyplot.xlabel("Valeurs obtenues")
    pyplot.ylabel("Occurences")
    pyplot.text(min(abscisses), max(ordonnees),
                r'$\mu=' + str(round(average, 5)) + ',\ \sigma=' + str(round(sigma, 5)) + '$')
    pyplot.title(
        str(n) + (" lancers" if n > 1 else "lancers") + " de " + str(k) + (" dé" if k < 2 else " dés") + " à " +
        str(p) + (" faces" if p > 1 else " face"))
    pyplot.show()

    return sigma


amount = int(input("Saisir le nombre d'expériences : "))
n = int(input("Saisir le nombre de lancers : "))
k = int(input("Saisir le nombre de dés : "))
p = int(input("Saisir le nombre de faces des dés : "))

sigmas = [0] * amount

i = 0
while i < amount:
    sigmas[i] = graphique(n, k, p)
    i += 1

print("Écart-type moyen :", sum(sigmas)/len(sigmas))
