def findDisappearedNumbers(nums):
    a = set(nums)
    b = set(range(1, len(nums) + 1))

    c = b - a
    c = list(c)
    return c

nums = [4,3,2,7,8,2,3,1]
# nums = [1, 1]
print (findDisappearedNumbers(nums))
