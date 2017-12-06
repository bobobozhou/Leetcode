def fizzBuzz(n):

    ## solution 1
    # lis = range(1, n + 1)
    #
    # for i in range(len(lis)):
    #
    #     n = lis[i]
    #
    #     if n % 3 == 0 and n % 5 == 0 and n % 15 == 0:
    #         lis[i] = 'FizzBuzz'
    #
    #     if n % 3 == 0 and n % 5 != 0 and n % 15 != 0:
    #         lis[i] = 'Fizz'
    #
    #     if n % 3 != 0 and n % 5 == 0 and n % 15 != 0:
    #         lis[i] = 'Buzz'
    #
    #     lis[i] = str(lis[i])
    #
    # return lis

    ## solution 2
    a = ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n + 1)]
    return a



print (fizzBuzz(15))

