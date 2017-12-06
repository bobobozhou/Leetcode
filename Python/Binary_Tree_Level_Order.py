# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrderBottom2(root):

# use stack to store the node value and level
# use this information to determine where to put in the result
    stack = [(root, 0)]
    res = []

    while stack:
        node, level = stack.pop()

        if node:
            if len(res) < level + 1:
                res.insert(0, [])

            res[-(level + 1)].append(node.val)

            stack.append((node.right, level + 1))
            stack.append((node.left, level + 1))

    return res




a = TreeNode(3)
a.left = TreeNode(9)
# a.left.left = TreeNode(10)
# a.left.right = TreeNode(11)

a.right = TreeNode(20)
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)

print (levelOrderBottom2(a))
