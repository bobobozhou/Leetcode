# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def forward(root):
            stack = []
            p = root
            while p:
                stack.append(p)
                p = p.left

            while stack:
                yield stack[-1].val
                p = stack[-1].pop().right

                while p:
                    stack.append(p)
                    p = p.left

            yield None

        def backward(root):
            stack = []
            p = root
            while p:
                stack.append(p)
                p = p.right

            while stack:
                yield stack[-1].val
                p = stack[-1].pop().left

                while p:
                    stack.append(p)
                    p = p.right

            yield None


        forward = forward(root)
        backward = backward(root)

        f, b = next(forward), next(backward)

        while f is not None is not b:
            if f == b:
                break

            if f + b > k:
                b = next(backward)

            else:
                f = next(forward)

        return False


a = TreeNode(5)
a.left = TreeNode(8)
a.left.left = TreeNode(9)
a.right = TreeNode(4)

print (Solution().findTarget(a, 9))
