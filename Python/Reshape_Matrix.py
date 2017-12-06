def matrixReshape(nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """

    if len(nums) * len(nums[0]) != r * c:
        return nums

    vals = []
    for row in nums:
        for ele in row:
            vals.append(ele)

    ans = [[None] * c for _ in range(r)]
    i = 0
    for nr in range(r):
        for nc in range(c):
            ans[nr][nc] = vals[i]
            i += 1

    return ans


nums = [[1, 2], [3, 4]]
r = 4
c = 1

print (matrixReshape(nums, r, c))


