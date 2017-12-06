def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    zero_pointer = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero_pointer] = nums[zero_pointer], nums[i]
            zero_pointer += 1


    return nums

print (moveZeroes([0,1,12,0,2]))
