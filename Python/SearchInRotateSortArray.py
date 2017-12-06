
def search (nums, tar):
    lo = 0
    hi = len(nums)

    while lo < hi:
        mid = (lo + hi)/2

        if (tar < nums[0]) == (nums[mid] < nums[0]):
            num = nums[mid]
        else:
            if tar >= nums[0]:
                num = float('inf')
            else:
                num = -float('inf')

        if num > tar:
            hi = mid
        else:
            if num < tar:
                lo = mid + 1
            else:
                return mid


    return -1



nums = [3,1]

print (search(nums, 3))

