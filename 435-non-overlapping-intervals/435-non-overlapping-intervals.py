class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        i, ans = 1, 0
        while i < len(intervals):
            if (intervals[i-1][0] <= intervals[i][0] and intervals[i-1][1] > intervals[i][0]):
                if (intervals[i][1] > intervals[i-1][1]):
                    intervals.pop(i)
                else:
                    intervals.pop(i-1)
                ans += 1
            else:
                i += 1
            
        return ans
    
    
        '''
            ans = 1
            [[1,2],[1,2]]
                     i
        '''