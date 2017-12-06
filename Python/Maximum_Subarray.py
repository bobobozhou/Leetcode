def maxSubArray(nums):

    if not nums:
        return 0

    cur_sum = nums[0]
    lar_sum = nums[0]

    for num in nums[1:]:
        cur_sum = max(num, cur_sum + num)
        lar_sum = max(lar_sum, cur_sum)

    return lar_sum


a1 = [-2,1,-3,4,-1,2,1,-5,4]
a2 = [1]
print (maxSubArray(a1))
