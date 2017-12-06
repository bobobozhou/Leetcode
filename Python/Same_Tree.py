# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSameTree(p, q):

    while p and q:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(q.right, q.right)

    return p == q


p = TreeNode(None)
q = TreeNode(0)

print (isSameTree(p, q))





