class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_map = self.genNumMap(nums)
        l_streak = 0
        for num in nums:
            if not (num - 1 in num_map):
                c_streak = 0
                while num in num_map:
                    c_streak += 1
                    num = num + 1
                l_streak = max(l_streak, c_streak)
        return l_streak
                    
                
    
    def genNumMap(self, nums):
        numMap = {}
        for num in nums:
            numMap[num] = True
        return numMap