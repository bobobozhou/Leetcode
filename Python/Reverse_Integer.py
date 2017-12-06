def reverse(x):
    if x < 0:
        return -reverse(-x)
    result = 0
    while x:
        result = 10 * result + x % 10
        x /= 10
    return result if result < 0x7FFFFFFF else 0


def reverse2(x):
    if x < 0:
        y = str(x)[::-1]
        z1 = y[-1]
        z2 = y[:-1]
        x = int(z1 + z2)
    else:
        x = int(str(x)[::-1])

    if abs(x) > 0x7FFFFFFF:
        x = 0

    return x


x = 56789
print (reverse(x))
print (reverse2(x))
