def removeDuplicates(nums):

    s = 0
    for i in range(len(nums)):
        if i == 0 or nums[i-1] != nums[i]:
            nums[s] = nums[i]
            s += 1

    a = nums[:s]
    return len(a)


NUMS = [1,1,1,2,2,3]
print (removeDuplicates(NUMS))