def nb_pairs(lst):
    """
    Retourne les nombres pairs compris dans une liste.
    :param lst: (lst) Liste d'entiers.

    >>> nb_pairs([1, 2, 3, 4, 5])
    2
    4
    """
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            print(lst[i])
        i += 1


def tous_pairs(lst):
    """
    Détermine si tous les nombres d'une liste sont pairs.
    :param lst: (lst) Liste d'entiers.
    :returns (bool) Résultat.

    >>> tous_pairs([1, 3, 5])
    False

    >>> tous_pairs([2, 4, 6])
    True
    """
    i = 0
    while i < len(lst):
        if lst[i] % 2 != 0:
            return False
        i += 1
    return True


def existe_pair(lst):
    """
    Détermine si au moins un nombre de la liste est pair.
    :param lst: (lst) Liste d'entiers.
    :return: (bool) Résultat.

    >>> existe_pair([1, 2, 3, 5, 7])
    True
    """
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            return True
        i += 1
    return False


def infos_liste(lst):
    """
    Retourne le nombre de pairs et d'impairs de la liste lst.
    :param lst: (lst) Liste d'entiers.
    :return: (tuple) Résultat.

    >>> infos_liste([1, 2, 3, 4, 5, 6])
    (3, 3)
    """
    pairs, impairs = 0, 0
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            pairs += 1
        else:
            impairs += 1
        i += 1
    return pairs, impairs


def pairs(lst):
    """
    Retourne une liste de pairs compris dans la liste lst.
    :param lst: (lst) Liste d'entiers.
    :return: (lst) Liste d'entiers pairs.

    >>> pairs([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    """
    result = []
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            result.append(lst[i])
        i += 1
    return result


def pairs_impairs(lst):
    """
    Retourne une liste contenant une liste des pairs et une liste des impairs de la liste lst.
    :param lst: (lst) Liste d'entiers.
    :return: (lst) Liste des pairs et des impairs.

    >>> pairs_impairs([1, 2, 3, 4, 5, 6])
    [[2, 4, 6], [1, 3, 5]]
    """
    pairs, impairs = [], []
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            pairs.append(lst[i])
        else:
            impairs.append(lst[i])
        i += 1
    return [pairs, impairs]
