def removeElement(nums, val):

    for x in nums[:]:
        if val == x:
            nums.remove(x)

    return len(nums)


nums = [3,3]
val = 3

print (removeElement(nums, val))