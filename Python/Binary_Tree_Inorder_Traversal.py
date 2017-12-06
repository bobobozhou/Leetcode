class treeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class solution(object):
    # iterative method
    def inorderTraversal1(self, root):
        stack = []
        res = []

        while True:
            while root:
                stack.append(root.left)
                root = root.left

            while not stack:
                return res

            node = stack.pop()
            res.append(node.val)
            root = node.right

    # recursive method
    def inorderTraversal2(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
            