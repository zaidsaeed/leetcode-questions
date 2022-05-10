class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        oneAns = self.findMax(nums[0:len(nums)-1])
        twoAns = self.findMax(nums[1:])
        return max(oneAns, twoAns)
        
    def findMax(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        ans = [0 for i in range(len(nums))]
        ans[0] = nums[0]
        ans[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            ans[i] = max(ans[i-1], ans[i-2] + nums[i])
        
        return ans[-1]