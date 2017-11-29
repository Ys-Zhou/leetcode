# 9 / 9 test cases passed.
# Runtime: 82 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        def cnode(val, left, right):
            node = TreeNode(val)
            node.left = left
            node.right = right
            return node

        def btree(start, end):
            if start > end:
                return []
            return [cnode(root, left, right)
                    for root in range(start, end + 1)
                    for left in btree(start, root - 1)
                    for right in btree(root + 1, end)]

        return btree(1, n)
