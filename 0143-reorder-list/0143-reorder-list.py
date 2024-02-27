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
        if not head or not head.next:
            return head
            
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        prevPtr, ptr = None, slow.next
        
        slow.next = None
        while ptr:
            oldNext = ptr.next
            ptr.next = prevPtr
            prevPtr = ptr
            ptr = oldNext
        
        head1, head2 = head.next, prevPtr
        ans, ptr = head, head
        i = 1
        while head1 and head2:
            if i % 2 != 0:
                ptr.next = head2
                head2 = head2.next
            else:
                ptr.next = head1
                head1 = head1.next
            ptr = ptr.next
            i += 1

        if head1:
            ptr.next = head1
        else:
            ptr.next = head2
            
        return ans
        
            