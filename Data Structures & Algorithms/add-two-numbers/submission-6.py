# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first, second = '', ''
        p1, p2 = l1, l2

        while p1:
            first += str(p1.val)
            p1 = p1.next
        while p2:
            second += str(p2.val)
            p2 = p2.next

        l_sum = int(first[::-1]) + int(second[::-1])
        l_sum = str(l_sum)[::-1]
        dummy = ListNode(0)

        builder = dummy
        for i in range(len(str(l_sum))):
            builder.next = ListNode(str(l_sum)[i])
            builder = builder.next
        
        return dummy.next