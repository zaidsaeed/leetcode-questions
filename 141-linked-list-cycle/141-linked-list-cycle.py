# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr = head
        while ptr is not None:
            if isinstance(ptr.val, bool) and ptr.val == True:
                return True
            ptr.val = True
            ptr = ptr.next
        return False
        