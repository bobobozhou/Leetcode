def checkPerfectNumber(num):
    """
    :type num: int
    :rtype: bool
    """
    if num <= 0:
        return False

    r = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            r = r + i + num // i

    if num == i**2:
        r = r - i

    r = r - num

    return r == num


print (checkPerfectNumber(28))