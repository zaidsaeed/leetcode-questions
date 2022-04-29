# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodeMap = {}
        n = 0
        ptr = head
        while ptr is not None:
            nodeMap[n] = ptr
            ptr = ptr.next
            n += 1
        
        ptr = head
        s = 1
        e = n - 1
        eTurn = True

        while e >= s:
            if not eTurn:
                ptr.next = nodeMap[s]
                s = s + 1
                eTurn = True
            else:
                ptr.next = nodeMap[e]
                e = e - 1
                eTurn = False
            ptr = ptr.next
        
        ptr.next = None
        
        
            