# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None
        prev = None
        curr = second
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        curr1, curr2 = head, prev
        dummy = ListNode(0)
        create = dummy
        while curr1 or curr2:
            create.next = curr1
            create = create.next
            curr1 = curr1.next
            if curr2:
                create.next = curr2
                create = create.next
                curr2 = curr2.next
                
        return

            
