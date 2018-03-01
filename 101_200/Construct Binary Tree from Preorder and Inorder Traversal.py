# 203 / 203 test cases passed.
# Runtime: 126 ms


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def c_tree(idx, start, end):
            if start == end:
                return None
            root = TreeNode(preorder[idx])
            root_idx = inorder.index(preorder[idx])
            root.left = c_tree(idx + 1, start, root_idx)
            root.right = c_tree(idx + 1 + root_idx - start, root_idx + 1, end)
            return root

        return c_tree(0, 0, len(preorder))
