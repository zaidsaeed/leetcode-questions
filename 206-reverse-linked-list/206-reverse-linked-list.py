# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            a = None
            b = head
            if not b.next: ##only one elem
                return b
            c = head.next
            while b:
                b.next = a
                a = b
                b = c
                if c:
                    c = c.next
            return a
        return head
                
        