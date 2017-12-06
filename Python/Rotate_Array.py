def rotate(nums, k):

    while k > 0:
        nums.insert(0, nums.pop())
        k -= 1

    return nums


nums = [1,3,4]
k = 1
print (rotate(nums, k))
