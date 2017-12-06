def addDigits(num):
    """
    :type num: int
    :rtype: int
    """

    def Digit_SUM(num):
        l = list(str(num))
        l_num = map(int, l)
        return sum(l_num)

    while len(list(str(Digit_SUM(num)))) != 1:
        num = Digit_SUM(num)

    return Digit_SUM(num)

print (addDigits(38))