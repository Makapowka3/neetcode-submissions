# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        counter = 0
        while counter != left - 1:
            p1 = p1.next
            counter += 1
        prev = p1.next
        curr = prev.next
        counter += 2
        while counter < right:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            counter += 1
        next_node = curr.next
        curr.next = prev
        p1.next.next = next_node
        p1.next = curr
        head = dummy.next
        return head
        