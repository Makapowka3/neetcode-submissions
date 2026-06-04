# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(current_node):
            if current_node is None:
                return
            res.append(current_node.val)
            traverse(current_node.left)
            traverse(current_node.right)
        
        traverse(root)
        return res