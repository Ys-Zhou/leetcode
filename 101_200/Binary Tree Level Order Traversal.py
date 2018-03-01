# 34 / 34 test cases passed.
# Runtime: 92 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        q = Queue.Queue()
        nowlvl = 0
        q.put([root, 1])
        while not q.empty():
            node = q.get()
            if node[1] == nowlvl:
                res[-1].append(node[0].val)
            else:
                res.append([node[0].val])
                nowlvl = node[1]
            if node[0].left:
                q.put([node[0].left, node[1] + 1])
            if node[0].right:
                q.put([node[0].right, node[1] + 1])
        return res
