def quicksort(nums):
    if len(nums) <= 1:
        return nums

    less = []
    equal = []
    greater = []

    pivot = nums[0]
    for n in nums:
        if n < pivot:
            less.append(n)

        if n == pivot:
            equal.append(n)

        if n > pivot:
            greater.append(n)

    return sorted(less) + equal + sorted(greater)


a = [2, 1, 4, 2, 3]
print (quicksort(a))
