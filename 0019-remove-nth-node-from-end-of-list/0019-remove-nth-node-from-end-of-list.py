# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        numOfNodes, nodesMap = self.getNodesData(head)
        nodeToRemove = (numOfNodes - n)
        if nodeToRemove == 0:
            return nodesMap.get(1, None)
        else:
            if nodeToRemove + 1 < numOfNodes:
                nodesMap[(nodeToRemove-1)].next = nodesMap[(nodeToRemove+1)]
            else:
                nodesMap[(nodeToRemove-1)].next = None
                
            return head
        
    def getNodesData(self, head):
        ptr, count = head, -1
        nodesMap = {}
        while ptr:
            count += 1
            nodesMap[count] = ptr
            ptr = ptr.next
        return (count+1), nodesMap