# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l = []
        def traverse(root):
            if not root:
                return
            
            if not root.left and not root.right:
                l.append(root.val)
            
            traverse(root.left)
            traverse(root.right)

        traverse(root1)
        traverse(root2)

        if len(l) % 2 != 0: return False
        p1, p2 = 0, len(l) // 2
        while p2 < len(l):
            if l[p1] != l[p2]:
                return False
            p1 += 1
            p2 += 1
        
        return True
        