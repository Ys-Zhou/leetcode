# 109 / 109 test cases passed.
# Runtime: 143 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue


class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            newNode = TreeNode(v)
            newNode.left = root
            return newNode
        # [<node>, <level>]
        q = Queue.Queue()
        q.put([root, 2])
        while not q.empty():
            now = q.get()
            if now[1] < d:
                if now[0].left:
                    q.put([now[0].left, now[1] + 1])
                if now[0].right:
                    q.put([now[0].right, now[1] + 1])
            else:
                newNode = TreeNode(v)
                newNode.left = now[0].left
                now[0].left = newNode
                newNode = TreeNode(v)
                newNode.right = now[0].right
                now[0].right = newNode
        return root
