# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy
        prev.next = head
        curr = head
        
        list_len = 0
        p1 = head
        while p1:
            list_len += 1
            p1 = p1.next
        
        for _ in range(list_len-n):
            curr = curr.next
            prev = prev.next
        
        prev.next = curr.next
        return dummy.next