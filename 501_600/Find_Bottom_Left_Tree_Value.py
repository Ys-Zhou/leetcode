# 74 / 74 test cases passed.
# Runtime: 132 ms
import Queue


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = Queue.Queue()
        q.put(root)
        now = None
        while not q.empty():
            now = q.get()
            if now.right:
                q.put(now.right)
            if now.left:
                q.put(now.left)
        return now.val
