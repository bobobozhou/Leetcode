def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    if len(set(nums)) == len(nums):
        return True

    return False

a = [1,2,3]
b = [1,1,2,3]
print (containsDuplicate(a))
print (containsDuplicate(b))