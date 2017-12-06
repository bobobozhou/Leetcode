def mergesort(nums):

    if len(nums) == 1:
        return nums

    mid = len(nums) / 2
    left = nums[:mid]
    right = nums[mid:]

    left = mergesort(left)
    right = mergesort(right)

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
            k += 1

        else:
            nums[k] = right[j]
            j += 1
            k += 1

    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

    return nums


a = [2, 1, 4, 3, 5]

print (mergesort(a))
