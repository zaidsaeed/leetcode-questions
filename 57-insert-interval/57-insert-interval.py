class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = 0, len(intervals) - 1
        lFound, rFound = False, False
        while l <= r:
            lInterval = intervals[l]
            rInterval = intervals[r]
            if newInterval[0] <= lInterval[1]:
                if not lFound:
                    lFound = lInterval
            if newInterval[1] >= rInterval[0]:
                if not rFound:
                    rFound = rInterval
                    
            if lFound and rFound:
                break
            if not lFound:
                l += 1
            if not rFound:
                r -= 1

        if lFound and rFound:
            for i in range(l, r+1):
                intervals.pop(l)
            intervals.insert(l, [min(lFound[0], newInterval[0]), max(rFound[1], newInterval[1])])
        else:
            index = 0
            while index < len(intervals) and intervals[index][1] < newInterval[0]:
                index += 1
            intervals.insert(index, newInterval)

        return intervals
    
    
    
    ###. [[3,4],[7,10]] newInterval = [7,8]
    ###    r l