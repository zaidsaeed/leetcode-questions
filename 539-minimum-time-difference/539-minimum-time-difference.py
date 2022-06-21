class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        nums = []
        
        for tp in timePoints:
            nums.append(self.convertToNum(tp))
        
        buckets, over = self.generateBucket(nums)
        
        if over:
            return 0
        
        ans = float('inf')
        
        for num in nums:
            numClosest = self.findClosestTp(buckets, num)
            ans = min(ans, numClosest)
        
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
                

        
        #search right
        i = num + 1
        if i == 1440:
            i = 0
        found = buckets[i] == 1
        countRight = 1
        while not found:
            countRight += 1
            i += 1
            if i == 1440:
                i = 0
            found = buckets[i] == 1

        
        return min(countLeft, countRight)
    
    def convertToNum(self, tp):
        mins = int(tp[3] + tp[4])
        hrs = int(tp[0] + tp[1])
        return (hrs * 60) + mins
    
    def generateBucket(self, nums):
        buckets = [0 for i in range(0, 1440)]
        for num in nums:
            if buckets[num] == 1:
                return None, True
            buckets[num] += 1
        return buckets, False