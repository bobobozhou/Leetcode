def searchInsert(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right)/2

        if nums[mid] < target:
            left = mid + 1

        elif nums[mid] > target:
            right = mid - 1

        elif nums[mid] == target:
            return mid

    return left

nums = [1, 4, 5, 8, 9, 10, 13]
target = 7
print (searchInsert(nums, target))

