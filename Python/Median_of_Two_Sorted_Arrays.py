def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    nums = sorted(nums1 + nums2)
    l = len(nums)
    if l % 2 == 0:
        return float(nums[l / 2 - 1] + nums[l / 2]) / 2

    if l % 2 == 1:
        return float(nums[l / 2])


nums1 = [1,2]
nums2 = [3,4]

print (findMedianSortedArrays(nums1,nums2))