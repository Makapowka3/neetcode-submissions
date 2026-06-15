# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #Find middle
        #Reverse the second half
        #Find and store the max twin sum

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = slow
        curr = slow.next
        prev.next = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        res = 0
        p1, p2 = head, prev
        while p1 and p2:
            res = max(res, p1.val + p2.val)
            p1 = p1.next
            p2 = p2.next
        
        return res