def majorityElement(nums):

    nums.sort()
    n = nums[len(nums)/2]

    return n


nums = [2, 2, 2, 3, 1, 4, 3, 2, 2, 2]
print(majorityElement(nums))
