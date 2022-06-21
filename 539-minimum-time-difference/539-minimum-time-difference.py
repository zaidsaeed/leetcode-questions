class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        nums = []
        
        for tp in timePoints:
            nums.append(self.convertToNum(tp))
        
        nums.sort()
        
        ans = float('inf')
        for i in range(1, len(nums)):
            ans = min(ans, abs(nums[i] - nums[i-1]))
        
        ans = min(ans, (1440 - nums[-1] + nums[0]))
        
        return ans
    
    def convertToNum(self, tp):
        mins = int(tp[3] + tp[4])
        hrs = int(tp[0] + tp[1])
        return (hrs * 60) + mins