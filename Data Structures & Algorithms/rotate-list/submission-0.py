# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 1
        p1 = head
        if not p1 or not p1.next:
            return p1

        while p1.next:
            p1 = p1.next
            length += 1
        p1.next = head
        rotate = length - (k % length)
        
        p1 = head.next
        p2 = head
        while rotate != 1:
            p1 = p1.next
            p2 = p2.next
            rotate -= 1
        
        p2.next = None
        return p1
        
