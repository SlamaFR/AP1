def inserer_trie(lst, x):
    """
    Insère l'entier x dans une liste triée.
    :param lst: (lst) Liste triée.
    :param x: (int) Entier.

    >>> inserer_trie([0, 1, 3], 2)
    """
    i = 0
    while i < len(lst):
        if x < lst[i]:
            lst.insert(i, x)
            return
        i += 1
    lst.append(x)


def inserer_tous(lst):
    """
    Insère les élements de lst de manière triée dans une nouvelle liste.
    :param lst: (lst) Liste.
    :return: (lst) Liste triée contenant les élements de lst.

    >>> inserer_tous([4, 1, 6, 2])
    [1, 2, 4, 6]
    """
    i = 0
    result = []
    while i < len(lst):
        inserer_trie(result, lst[i])
        i += 1
    return result
