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
        temp = Node(0)
        n = temp
        p2 = temp
        p1 = head
        while p1 is not None:
            p2.next = Node(p1.val)
            hash_map[p1] = p2.next
            p2 = p2.next
            p1 = p1.next

        p1 = head
        while p1 is not None:
            if p1.random is None:
                temp.next.random = None
            else:
                temp.next.random = hash_map[p1.random]
            temp = temp.next
            p1 = p1.next
        new_head = n.next
        n.next = None
        return new_head
              
            