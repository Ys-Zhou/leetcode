# 203 / 203 test cases passed.
# Runtime: 132 ms


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        def tree(p_root, i_start, i_end):
            if i_end == i_start:
                return None
            i_root = inorder.index(postorder[p_root])
            root = TreeNode(postorder[p_root])
            root.right = tree(p_root - 1, i_root + 1, i_end)
            root.left = tree(p_root - i_end + i_root, i_start, i_root)
            return root

        return tree(len(postorder) - 1, 0, len(inorder))
