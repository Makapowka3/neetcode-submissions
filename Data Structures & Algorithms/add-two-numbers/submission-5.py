# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        p1, p2 = l1, l2
        while p1 or p2 or carry:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0

            carry, digit = divmod(v1 + v2 + carry, 10)

            cur.next = ListNode(digit)
            cur = cur.next

            if p1: p1 = p1.next
            if p2: p2 = p2.next

        return dummy.next
        
        