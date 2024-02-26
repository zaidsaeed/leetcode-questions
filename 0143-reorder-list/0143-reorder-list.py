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
        ptr, cnt = head, 1
        while ptr:
            prevPtr = ptr
            nodeMap[cnt] = ptr
            cnt += 1
            ptr = ptr.next
            prevPtr.next = None
        
        numNodes = cnt - 2
        idx = 1
        res, ptr = nodeMap[idx], nodeMap[idx]
        leftSide = False
        while numNodes != 0:
            if leftSide:
                ptr.next = nodeMap[idx]
            else:
                ptr.next = nodeMap[cnt - idx]
                idx += 1
            leftSide = not leftSide
            ptr = ptr.next
            numNodes -= 1
        
        # ptr = res
        # while ptr:
        #     print(ptr.val)
        #     ptr = ptr.next
        
        return res
            