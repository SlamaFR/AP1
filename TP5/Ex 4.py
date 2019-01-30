def supprime_min(lst):
    """
    Supprime et retourne la plus petite valeur de la liste.
    :param lst: (lst) Liste.
    :returns (int) Valeur supprimée.

    >>> supprime_min([1, 2, 4, 5])
    1
    """
    return lst.pop(lst.index(min(lst)))


def plus_petits(lst, n):
    """
    Retourne une liste contenant les n plus petites valeurs de la liste.
    :param lst: (lst) Liste.
    :param n: (int) Entier positif.
    :returns (lst) Liste contenant les n plus petites valeurs de la liste.

    >>> plus_petits([1, 2, 3, 4], 2)
    [1, 2]
    """
    original = lst * 1
    result = []
    i = 0
    while i < n:
        result.append(supprime_min(original))
        i += 1
    return result
