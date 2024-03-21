class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        idxToAdd = 0
        if intervals and newInterval[0] > intervals[0][1]:
            idxToAdd = n
        for i in range(n-1):
            interval = intervals[i]
            nextInterval = intervals[i+1]
            if (interval[0] <= newInterval[0]) and (nextInterval[0] >= newInterval[0]):
                idxToAdd = (i + 1)
                break
        intervals.insert(idxToAdd, newInterval)
        self.mergeOverlappingIntervals(intervals)
        return intervals
    
    def mergeOverlappingIntervals(self, intervals):
        i = 0
        while i < len(intervals)-1:
            interval1, interval2 = intervals[i], intervals[i+1]
            if interval2[0] <= interval1[1]:
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i, [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])])
            else:
                i += 1
        