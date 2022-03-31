# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        ansHead = None
        ptr = None
        count = len(lists)
        
        def createHeap(heads):
            heap = []
            for i in range(len(heads)):
                head = heads[i]
                if head:
                    heap.append((head.val,i, head))
            heapq.heapify(heap)
            return heap
        
        def printRes(ansHead):
            ptr = ansHead
            while ptr:
                print(ptr.val)
                ptr = ptr.next
        
        heap = createHeap(lists)
        while heap:
            node = heapq.heappop(heap)[2]
            
            if not ansHead:
                ansHead = node
                ptr = node
            else:
                ptr.next = node
                ptr = ptr.next
                
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, count, node))
                count += 1
            
        return ansHead            