from collections import Counter
import math

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        charArr = [0 for i in range(len(s))]
        countsArr = counts.most_common()
        countsArr = [(-1*val, key) for (key, val) in countsArr]
        heapq.heapify(countsArr)
        i = 0
        while len(countsArr) > 0:
            most_comm = heapq.heappop(countsArr)
            most_comm1 = None
            if len(countsArr) > 0:
                most_comm1 = heapq.heappop(countsArr)
            elif most_comm[0] != -1:
                return ""
            charArr[i] = most_comm[1]
            i += 1
            if most_comm1:
                charArr[i] = most_comm1[1]
                i += 1
            most_comm = (most_comm[0] + 1, most_comm[1])
            if most_comm1:
                most_comm1 = (most_comm1[0] + 1, most_comm1[1])
            if most_comm[0] != 0:
                heapq.heappush(countsArr, most_comm)
            if most_comm1 and most_comm1[0] != 0:
                heapq.heappush(countsArr, most_comm1)
        return ''.join(charArr)
            