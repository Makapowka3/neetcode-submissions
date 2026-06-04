# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2

        dummy = ListNode(0)
        head3 = dummy

        while p1 is not None and p2 is not None:
            if p1.val > p2.val:
                dummy.next = p2
                p2 = p2.next
            else:
                dummy.next = p1
                p1 = p1.next
            dummy = dummy.next

        while p1 is not None:
            dummy.next = p1
            p1 = p1.next
            dummy = dummy.next
        
        while p2 is not None:
            dummy.next = p2
            p2 = p2.next
            dummy = dummy.next
        
        temp = head3.next
        head3.next = None
        return temp
        
