# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_count = 0
        p1 = head

        while p1:
            p1 = p1.next
            len_count += 1
        
        node_rmv = len_count - n + 1
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        for _ in range(node_rmv-1):
            prev = prev.next
            curr = curr.next
        
        prev.next = curr.next
        return dummy.next