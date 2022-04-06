class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = [float('-inf') for i in range(len(nums))]
        ans[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            ans[i] = max(nums[i], ans[i-1] + nums[i])
            res = max(ans[i], res)
        return res
    
    # [-2,1,-3,4,-1,2,1,-5,4]
    # [-2,1,-2,4,3,5,6,1,5 ]