# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p_A = headA
        p_B = headB
        
        while p_A is not p_B:
            p_A = p_A.next if p_A else headB
            p_B = p_B.next if p_B else headA

        return p_A