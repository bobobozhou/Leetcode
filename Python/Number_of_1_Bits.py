def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """

    if not n:
        return 0

    count = 0

    for _ in range(32):
        a = n & 1
        if a == 1:
            count += 1
        n = n >> 1

    return count


print (hammingWeight(11))
