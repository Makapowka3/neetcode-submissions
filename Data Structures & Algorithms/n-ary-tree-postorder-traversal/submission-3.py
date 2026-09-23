"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res = []

        def traverse(current_node):
            children = current_node.children
            for c in children:
                traverse(c)
            res.append(current_node.val)
        
        traverse(root)
        return res