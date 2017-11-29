# 74 / 74 test cases passed.
# Runtime: 59 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check(min_, max_, tree):
            if not tree:
                return True
            if tree.left and (tree.left.val >= tree.val or tree.left.val <= min_):
                return False
            if tree.right and (tree.right.val <= tree.val or tree.right.val >= max_):
                return False
            return check(min_, tree.val, tree.left) and check(tree.val, max_, tree.right)

        return check(float('-inf'), float('inf'), root)
