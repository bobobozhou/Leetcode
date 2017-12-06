# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def minDepth(root):
    if not root:
        return 0

    d = sorted([minDepth(root.left), minDepth(root.right)])

    return 1 + (min(d) or max(d))



