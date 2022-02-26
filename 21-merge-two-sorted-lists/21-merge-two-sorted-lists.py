# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        ptr = None
        if list1 and list2:
            if list1.val > list2.val:
                head = list2
                list2 = list2.next
            else:
                head = list1
                list1 = list1.next
                
            ptr = head
            while list1 is not None and list2 is not None:
                if list1.val > list2.val:
                    ptr.next = list2
                    list2 = list2.next
                else:
                    ptr.next = list1
                    list1 = list1.next
                ptr = ptr.next
            
            if list1:
                ptr.next = list1
            else:
                ptr.next = list2
            
            return head   
        
        elif list1 and not list2:
            return list1
        else:
            return list2
            