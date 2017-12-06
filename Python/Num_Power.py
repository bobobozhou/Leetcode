def power1(x, y):

    if y == 0:
        return 1

    if y % 2 == 0:
        return power1(x, y / 2) * power1(x, y / 2)
    else:
        return x * power1(x, y / 2) * power1(x, y / 2)

print (power1(2, 4))