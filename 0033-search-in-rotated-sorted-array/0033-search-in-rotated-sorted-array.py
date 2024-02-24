class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minIdx = self.getMinIndex(nums)
        if nums[minIdx] <= target and nums[-1] >= target:
            res = self.binSearch(nums[minIdx:], target)
            if res < 0:
                return res
            return minIdx + res
        
        return self.binSearch(nums[0:minIdx], target)
    
    def binSearch(self, nums, target):
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + ((r-l)//2)
            
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
                
        return -1
    
    def getMinIndex(self, nums):
        l, r = 0, len(nums) - 1
        res = (nums[l], l)
        
        while l <= r:
            mid = l + ((r-l) // 2)
            
            if nums[mid] >= nums[l]:
                if nums[l] < res[0]:
                    res = (nums[l], l)
                l = mid + 1
            else:
                r = mid
                
        return res[1]
            