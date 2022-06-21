class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        nums, buckets = [], [0 for i in range(0, 1440)]
        
        for tp in timePoints:
            num = self.convertToNum(tp)
            nums.append(num)
            if buckets[num] == 1:
                return 0
            buckets[num] += 1
        
        i = 0
        while buckets[i] != 1:
            i += 1
        
        first = i
        
        i = 1439
        while buckets[i] != 1:
            i -= 1
        
        last = i
        

        ans = (1440 - last) + first
        
        for i in range(first + 1, len(buckets)):
            num = buckets[i]
            if num:
                ans = min(ans, i - first)
                first = i
        
        return ans
    
    
    def findClosestTp(self, buckets, num):
        #search left 
        i = num - 1
        if i == -1:
            i = 1439
        found = buckets[i] == 1
        countLeft = 1
        while not found:
            countLeft += 1
            i -= 1
            if i == -1:
                i = 1439
            found = buckets[i] == 1

        return countLeft
    
    def convertToNum(self, tp):
        mins = int(tp[3] + tp[4])
        hrs = int(tp[0] + tp[1])
        return (hrs * 60) + mins
    