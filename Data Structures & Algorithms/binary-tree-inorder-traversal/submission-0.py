# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(current_node):
            if not current_node:
                return
            traverse(current_node.left)
            res.append(current_node.val)
            traverse(current_node.right)
        
        traverse(root)
        return res