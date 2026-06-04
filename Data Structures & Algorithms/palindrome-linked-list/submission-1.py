# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None: return True
        temp = head
        if temp.next:
            p1 = temp.next
        else:
            return True
        while p1.next is not None:
            p1 = p1.next
            temp = temp.next
        if head.val == p1.val:
            temp.next = None
            return self.isPalindrome(head.next)
        else:
            return False