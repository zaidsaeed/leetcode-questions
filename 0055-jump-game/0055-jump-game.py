class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums) != 1:
            return False
        
        if nums:
            jumps = nums[0]
            for i in range(1, len(nums)-1):
                jumps -= 1
                cell = nums[i]
                jumps = max(jumps, cell)
                if jumps == 0:
                    return False
        return True