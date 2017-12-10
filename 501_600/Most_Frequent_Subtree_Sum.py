# 61 / 61 test cases passed.
# Runtime: 76 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        rec = {}

        def calsum(node):
            if not node:
                return 0
            subsum = node.val + calsum(node.left) + calsum(node.right)
            if subsum in rec:
                rec[subsum] += 1
            else:
                rec.setdefault(subsum, 1)
            return subsum

        calsum(root)
        maxsum = max(rec.values())
        res = []
        for k in rec:
            if rec[k] == maxsum:
                res.append(k)
        return res
