def premiers_entiers(a):
    """
    Retourne une liste des a premiers entiers.
    :param a: (int) Nombre.
    :return: (lst) Liste des a premiers entiers.

    >>> premiers_entiers(3)
    [0, 1, 2]
    """
    result = []
    i = 0
    while i < a:
        result.append(i)
        i += 1
    return result


def intervalle(a, b):
    """
    Retourne la liste des entiers compris entre a et b avec a < b.
    :param a: (int) Borne inférieure.
    :param b: (int) Borne supérieure.
    :return: (lst) Liste des entiers compris entre a et b.

    >>> intervalle(3, 7)
    [3, 4, 5, 6]
    """
    result = []
    i = a
    while i < b:
        result.append(i)
        i += 1
    return result


def intervalle_etendu(a, b, c):
    """
    Retourne une liste contenant les entiers compris entre a et b sous la forme a + k * c.
    :param a: (int) Borne inférieure.
    :param b: (int) Borne supérieure.
    :param c: (int) Entier.
    :return: (lst) Lite contenant les entiers compris entre a et b sous la form a + k * c.

    >>> intervalle_etendu(1, 5, 2)
    [1, 2, 3, 4]

    """
    result = []
    if c > 0:
        i = a
        while i < b:
            k = 0
            while i + k * c < b:
                if i + k * c not in result:
                    result.append(i + k * c)
                k += 1
            i += 1
    else:
        i = b - 1
        while i > a:
            k = 0
            while i + k * c > a:
                if i + k * c not in result:
                    result.append(i + k * c)
                k += 1
            i -= 1
    result.sort()
    return result


def tranche(lst, i, j, k):
    """
    Retourne les éléments de lst d'indices i à j - 1.
    :param lst: (lst) Liste.
    :param i: (int) Indice inférieur.
    :param j: (int) Indice supérieur.
    :param k: (int) pas
    :return: (lst) Liste des élements de lst d'indices i à j - 1.

    >>> tranche([0, 1, 2, 3, 4, 5], 2, 4, 1)
    [2, 3]
    """
    result = []
    while i < j:
        result.append(lst[i])
        i += k
    return result
