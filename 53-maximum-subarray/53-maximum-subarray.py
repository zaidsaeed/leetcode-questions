class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
            res = max(nums[i], res)
        return res
    
    # [-2,1,-3,4,-1,2,1,-5,4]
    # [-2,1,-2,4,3,5,6,1,5 ]