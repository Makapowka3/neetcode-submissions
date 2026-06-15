# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        p1, p2 = l1, l2

        while p1:
            stack1.append(p1.val)
            p1 = p1.next
        while p2:
            stack2.append(p2.val)
            p2 = p2.next
        
        carry = 0
        dummy = ListNode(0)
        builder = dummy
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10

            builder.next = ListNode(digit)
            builder = builder.next

        prev = None
        curr = dummy.next

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev      
