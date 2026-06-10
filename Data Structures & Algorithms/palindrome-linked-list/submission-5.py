# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        p1, p2 = 0, len(vals) - 1
        while p1 < p2:
            if vals[p1] != vals[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True
