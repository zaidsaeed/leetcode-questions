class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans = len(nums) - 1
        for i in range(len(nums)-2 , -1, -1):
            steps = nums[i]
            if i + steps >= ans:
                ans = i
        return ans == 0