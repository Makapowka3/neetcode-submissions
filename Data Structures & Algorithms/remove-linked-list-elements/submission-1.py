# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while curr:
            next_node = curr.next
            if curr.val == val:
                prev.next = next_node
                curr = next_node
            else:
                prev = prev.next
                curr = curr.next
        return dummy.next