# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums):

    if not nums:
        return None

    mid = len(nums) / 2

    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])

    return root



nums = [1, 2, 3, 4, 5, 6, 7]
print(sortedArrayToBST(nums))


