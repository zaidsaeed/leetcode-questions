from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = Counter(nums)
        heap = []
        for num, count in numsDict.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            else:
                currentMin = heapq.heappop(heap)
                if currentMin[0] > count:
                    heapq.heappush(heap, currentMin)
                else:
                    heapq.heappush(heap, (count, num))
        return [elem[1] for elem in heap]
        