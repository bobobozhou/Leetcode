def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    seen = set()

    while n not in seen:
        seen.add(n)
        n = sum([int(i)**2 for i in str(n)])

    return n == 1



print (isHappy(2))
