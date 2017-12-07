# 18 / 18 test cases passed.
# Runtime: 145 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dleft = dright = root
        cleft, cright = 0, 0
        while dleft:
            cleft += 1
            dleft = dleft.left
        while dright:
            cright += 1
            dright = dright.right
        if cleft == cright:
            return 2 ** cright - 1
        lefteage = 2 ** cright
        righteage = 2 ** cleft - 1
        while lefteage < righteage:
            mid = root
            midindi = (lefteage + righteage) / 2
            for branch in str(bin(midindi))[3:]:
                if branch == '0':
                    mid = mid.left
                else:
                    mid = mid.right
            if mid:
                lefteage = midindi + 1
            else:
                righteage = midindi
        return righteage - 1
