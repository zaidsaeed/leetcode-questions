class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [nums[i] for i in range(n)]
        if n <= 2:
            return max(nums)
        for i in range(n):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(nums[i], nums[i-1])
            else:
                dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        return dp[-1]