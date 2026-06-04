# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter1, counter2 = 0, 1
        current1, current2 = head, head
        while current1:
            counter1 += 1
            current1 = current1.next   
        if counter1 > 1:
            target_n = counter1 - n + 1
        else:
            head = None
            return head
        while counter2 < target_n - 1:
            counter2 += 1
            current2 = current2.next
        if target_n == 1:
            head = head.next
        else:
            current2.next = current2.next.next
        return head
