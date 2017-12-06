def findPairs(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums = sorted(nums)
    dict = {}
    res = []

    for i in range(len(nums)):
        if nums[i] - k in dict:
            res.append((nums[i] - k, nums[i]))

        dict[nums[i]] = i

    return res


nums = [1, 1, 1, 1, 1]
k = 0
print (findPairs(nums, k))