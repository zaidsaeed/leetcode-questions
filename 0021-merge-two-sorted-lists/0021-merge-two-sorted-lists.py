# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pt1, pt2 = list1, list2
        head, ans = None, None
        while pt1 and pt2:
            if pt1.val < pt2.val:
                if not head:
                    head = pt1
                    ans = head
                else:
                    head.next = pt1
                    head = head.next
                    
                pt1 = pt1.next
            else:
                if not head:
                    head = pt2
                    ans = head
                else:
                    head.next = pt2
                    head = head.next
                
                pt2 = pt2.next
            
        if pt1:
            if head:
                head.next = pt1
            else:
                head = pt1
                ans = head
        elif pt2:
            if head:
                head.next = pt2
            else:
                head = pt2
                ans = head

        return ans