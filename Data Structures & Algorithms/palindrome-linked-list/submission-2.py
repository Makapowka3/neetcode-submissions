# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = slow
        current = slow.next if slow.next else None

        while current:
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode
        
        slow.next = None

        p1, p2 = head, prev
        while p1 is not p2 and p1 is not None and p2 is not None:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        
        return True