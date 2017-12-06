def singleNumber1(nums):
    res = 0
    for n in nums:
        res = res ^ n

    return res


def singleNumber2(nums):
    a = set(nums)
    res = 2 * sum(a) - sum(nums)

    return res


def singleNumber3(nums):
    dict = {}

    for n in nums:
        dict[n] = dict.get(n, 0) + 1

    for key, val in dict.items():
        if val == 1:
            return key


nums = [2, 1, 3, 1, 2]
print (singleNumber3(nums))
