def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    last = 0
    now = 0

    for n in nums:

        last, now = now, max(last + n, now)

    return now


a = [1, 4, 0, 0, 5]

print (rob(a))

