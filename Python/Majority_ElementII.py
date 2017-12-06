def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums_set = set(nums)
    l = len(nums)
    ans = []

    for n in nums_set:
        if nums.count(n) > l / 3:
            ans.append(n)

    return ans

print (majorityElement([1,1,1,2,3,4,5,5,5,5,5]))
