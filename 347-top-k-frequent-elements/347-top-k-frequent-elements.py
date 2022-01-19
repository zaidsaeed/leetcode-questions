from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heapPairs = [(value, key) for (key, value) in counts.items()]
        heap = heapPairs[0:k]
        heapq.heapify(heap)
        items = counts.items()
        for i in range(k, len(heapPairs)):
            item = heapPairs[i]
            minItem = heapq.heappop(heap)
            if minItem[0] < item[0]:
                heapq.heappush(heap, item)
            else:
                heapq.heappush(heap, minItem)
        return [item[1] for item in heap]