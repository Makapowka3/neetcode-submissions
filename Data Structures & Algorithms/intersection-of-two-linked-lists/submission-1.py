# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1, p2 = headA, headB
        counter_a, counter_b = 0, 0
        while p1.next is not None:
            p1 = p1.next
            counter_a += 1
        while p2.next is not None:
            p2 = p2.next
            counter_b += 1
        
        if p1 is not p2:
            return None
        
        diff = counter_a - counter_b
        p1, p2 = headA, headB
        if diff >= 0:
            while diff != 0:
                p1 = p1.next
                diff -= 1
        else:
            while diff != 0:
                p2 = p2.next
                diff += 1
        
        while p1 is not p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1
                