def twoSum(nums, target):

    dict = {}

    for i, num in enumerate(nums):

        if target - num in dict:
            return [dict[target - num], i]

        dict[num] = i

    return []

nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))