def mySqrt(x):

    if x == 0:
        return 0

    i = 0
    j = x/2 + 1

    while (j >= i):
        mid = (i + j)/2

        if mid ** 2 == x:
            return mid

        elif mid ** 2 > x:
            j = mid - 1

        elif mid ** 2 < x:
            i += mid + 1

    return j


print (mySqrt(8))