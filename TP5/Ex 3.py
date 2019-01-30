def est_croissante(lst):
    """
    Détermine si une liste lst est croissante.
    :param lst: (lst) Liste.
    :return: (bool) Résultat.

    >>> est_croissante([1, 2, 3, 4])
    True
    """
    i = 0
    while i < len(lst) - 1:
        if lst[i] > lst[i + 1]:
            return False
        i += 1
    return True


def est_triee(lst):
    """
    Détermine si une liste est triée.
    :param lst: (lst) Liste.
    :return: (bool) Résultat.

    >>> est_triee([1, 2, 3, 4])
    True

    >>> est_triee([4, 3, 2, 1])
    True

    >>> est_triee([1, 3, 2, 4])
    False
    """
    if est_croissante(lst):
        return True
    else:
        i = 0
        while i < len(lst) - 1:
            if lst[i] < lst[i + 1]:
                return False
            i += 1
        return True
