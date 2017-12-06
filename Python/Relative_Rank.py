def findRelativeRanks(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    sort = sorted(nums, reverse=True)
    rank = ['Gold Medal', 'Silver Medal', 'Bronze Medal'] + map(str, range(4, len(nums) + 1))
    d = zip(sort, rank)
    res = map(dict(d).get, nums)

    return res

print (findRelativeRanks([5,4,3,2,1]))