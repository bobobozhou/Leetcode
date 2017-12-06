def getSum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """

    for _ in range(32):
        a, b = a ^ b, (a & b) << 1

    if a & 0x80000000:
        return a
    else:
        return a & 0xffffffff

print (getSum(-1, 1))
