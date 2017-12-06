def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    ind_beg = 0
    ind_end = len(numbers) - 1

    while ind_beg < ind_end:
        if numbers[ind_beg] + numbers[ind_end] == target:
            return ind_beg + 1, ind_end + 1

        if numbers[ind_beg] + numbers[ind_end] > target:
            ind_end -= 1

        if numbers[ind_beg] + numbers[ind_end] < target:
            ind_beg += 1


print (twoSum([2, 7, 11, 15], 9))