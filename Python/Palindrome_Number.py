def isPalindrome1(x):
    if x < 0 | abs(x) > 0x7ffffff:
        return False

    y, reverse = x, 0

    while y:
        reverse *= 10
        reverse += y % 10
        y /= 10

    return x == reverse


def isPalindrome2(x):
    if (x < 0) | (abs(x) > 0x7fffffff):
        return False

    y = int(str(x)[::-1])
    return x == y


print (isPalindrome2(-12321))