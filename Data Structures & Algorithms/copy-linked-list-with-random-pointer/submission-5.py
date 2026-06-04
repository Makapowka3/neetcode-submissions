"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = {}
        dummy = Node(0)
        p2 = dummy
        p1 = head
        while p1 is not None:
            p2.next = Node(p1.val)
            hash_map[p1] = p2.next
            p2 = p2.next
            p1 = p1.next

        p1 = head
        p2 = dummy
        while p1 is not None:
            if p1.random is None:
                p2.next.random = None
            else:
                p2.next.random = hash_map[p1.random]
            p2 = p2.next
            p1 = p1.next
        new_head = dummy.next
        return new_head
              
            