# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        p1, p2 = dummy, head
        while p2:
            counter = 0
            while counter != m and p2:
                p2 = p2.next
                p1 = p1.next
                counter += 1
            counter = 0
            while counter != n and p2:
                p1.next = p2.next
                p2 = p2.next
                counter += 1
        return dummy.next