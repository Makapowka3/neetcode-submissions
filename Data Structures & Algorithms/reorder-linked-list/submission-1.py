# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p1 = head
        while p1 is not None and p1.next is not None:
            if p1.next.next is None:
                return
            p2 = p1
            while p2.next.next is not None:
                p2 = p2.next
            p2.next.next = p1.next
            p1.next = p2.next
            p2.next = None
            if p1.next is not None:
                p1 = p1.next.next