class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums = [num%2 for num in nums]
        even, odd, alternate = 0, 0, 0
        expected = nums[0]
        for i in range(len(nums)):
            num = nums[i]
            if num % 2 ==0:
                even += 1
            else:
                odd += 1
            if num == expected:
                alternate += 1
                expected = 1 - expected
        return max(even, odd, alternate)