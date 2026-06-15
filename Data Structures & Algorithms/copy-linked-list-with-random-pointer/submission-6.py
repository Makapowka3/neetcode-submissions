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
        hashmap = {None: None}
        p1 = head

        while p1:
            hashmap[p1] = Node(p1.val)
            p1 = p1.next
        
        current = head
        while current:
            hashmap[current].next = hashmap[current.next]
            hashmap[current].random = hashmap[current.random]
            current = current.next
        
        return hashmap[head]