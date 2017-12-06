def climbStairs(n):

    # if n == 1:
    #     return 1
    #
    # a = 1
    # b = 2
    # for _ in range(2, n):
    #     tem = b
    #     b = a + b
    #     a = tem
    #
    # return b


    if n == 1:
        return 1

    a = 1
    b = 2

    for _ in range(2, n):
        temp = b
        b = a + b
        a = temp

    return b


print (climbStairs(2))