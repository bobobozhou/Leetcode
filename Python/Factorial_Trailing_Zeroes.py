def trailingZeroes(n):
    """
    :type n: int
    :rtype: int
    """

    res = 0

    x = 5

    while n >= x:

        res = res + n / x
        x = x * 5

    return res

print (trailingZeroes(10))