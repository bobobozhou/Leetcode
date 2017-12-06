def search(nums, target):
    low = 0
    high = len(nums)
    while low < high:
        # middle = low + (high - low)/2
        middle = (low + high) / 2
        current = nums[middle] if (nums[middle] > nums[0]) == (target > nums[0]) else (
        -float('inf') if target <= nums[0] else float('inf'))
        if current < target:
            low = middle + 1
        elif current > target:
            high = middle
        else:
            return middle
    return -1


nums = [3,1]

print (search(nums, 3))