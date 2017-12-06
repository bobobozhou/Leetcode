def addBinary(a, b):

    aindex = len(a) - 1
    bindex = len(b) - 1
    flag = 0
    s = ''

    while aindex >= 0 and bindex >= 0:
        num = int(a[aindex]) + int(b[bindex]) + flag
        flag = num/2
        num = num % 2
        s = str(num) + s

        aindex -= 1
        bindex -= 1

    while aindex >= 0:
        num = int(a[aindex]) + flag
        flag = num/2
        num = num % 2
        s = str(num) + s

        aindex -= 1

    while bindex >= 0:
        num = int(b[bindex]) + flag
        flag = num / 2
        num = num % 2
        s = str(num) + s

        bindex -= 1

    if flag == 1:
        s = '1' + s

    return s

a = '11'
b = '1'

print (addBinary(a, b))
