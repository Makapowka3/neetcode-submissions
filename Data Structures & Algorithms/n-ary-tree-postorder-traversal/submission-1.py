"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        results = []
        if not root:
            return results
            
        def traverse(current_node):
            for node in current_node.children:
                traverse(node)
            results.append(current_node.val)
        
        traverse(root)
        return results