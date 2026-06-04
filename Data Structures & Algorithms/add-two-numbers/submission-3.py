# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        dummy = ListNode(0)
        p_build = dummy
        whole = 0
        while p1 is not None and p2 is not None:
            summ = p1.val + p2.val + whole
            whole = 0
            if summ >= 10:
                r = summ % 10
                whole = 1
            else:
                r = summ
            p_build.next = ListNode(r)
            p_build = p_build.next
            if p1.next is None and p2.next is None:
                if whole == 1:
                    p_build.next = ListNode(1)
            p1 = p1.next
            p2 = p2.next
        while p1 is not None:
            summ = p1.val + whole
            whole = 0
            if summ >= 10:
                r = summ % 10
                whole = 1
            else:
                r = summ
            p_build.next = ListNode(r)
            p_build = p_build.next
            if p1.next is None:
                if whole == 1:
                    p_build.next = ListNode(1)
            p1 = p1.next
        while p2 is not None:
            summ = p2.val + whole
            whole = 0
            if summ >= 10:
                r = summ % 10
                whole = 1
            else:
                r = summ
            p_build.next = ListNode(r)
            p_build = p_build.next
            if p2.next is None:
                if whole == 1:
                    p_build.next = ListNode(1)
            p2 = p2.next
        return dummy.next

            