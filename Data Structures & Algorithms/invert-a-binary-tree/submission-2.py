# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        left_p = root.left
        right_p = root.right
        self.invertTree(left_p)
        self.invertTree(right_p)
        root.left, root.right = root.right, root.left
        return root

