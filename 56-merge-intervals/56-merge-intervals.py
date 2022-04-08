class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def func(elem):
            return elem[0]
        
        sortedIntervals = sorted(intervals, key=func)
        i = 0
        while i + 1 < len(sortedIntervals):
            interval1 = sortedIntervals[i]
            interval2 = sortedIntervals[i+1]
            if interval2[0] >= interval1[0] and interval2[0] <= interval1[1]:
                sortedIntervals.pop(i)
                sortedIntervals.pop(i)
                sortedIntervals.insert(i, [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])])
            else:
                i += 1
        return sortedIntervals
    
    
    #   [ [1,5], [4,5] ]
    #       1      2
    #
    #