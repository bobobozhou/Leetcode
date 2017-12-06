def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    if len(nums) < 3:
        return []

    if len(nums) == 3 and sum(nums) == 0:
        return [sorted(nums)]

    nums = sorted(nums)
    r = []

    for i in range(len(nums) - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1

        while j < k:
            temp_sum = nums[i] + nums[j] + nums[k]

            if temp_sum == 0:
                r.append((nums[i], nums[j], nums[k]))

            if temp_sum > 0:
                k = k - 1

            else:
                j = j + 1

    return list(set(r))


print (threeSum([-1, 0, 1, 2, -1, -4]))
