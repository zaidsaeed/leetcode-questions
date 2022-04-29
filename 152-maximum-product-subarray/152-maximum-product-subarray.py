class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arrLen = len(nums) 
        if arrLen == 0:
            return 0
        absMin = nums[0]
        absMax = nums[0]
        ans = nums[0]
        for i in range(1, arrLen):
            minProd = absMin * nums[i]
            maxProd = absMax * nums[i]
            absMin = min(nums[i], min(minProd, maxProd))
            absMax = max(nums[i], max(minProd, maxProd))
            ans = max(ans, absMax)
        return ans
        