def judgeSquareSum(c):
    """
    :type c: int
    :rtype: bool
    """
    n = int(c ** 0.5)
    n_set = range(0, n + 1)

    ind_beg = 0
    ind_end = len(n_set) - 1

    while ind_beg <= ind_end:
        if n_set[ind_beg] ** 2 + n_set[ind_end] ** 2 == c:
            return True

        if n_set[ind_beg] ** 2 + n_set[ind_end] ** 2 > c:
            ind_end -= 1

        if n_set[ind_beg] ** 2 + n_set[ind_end] ** 2 < c:
            ind_beg += 1

    return False

print (judgeSquareSum(2))