class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        neededSum = 0
        for i in range(0, n+1):
            neededSum += i
        return neededSum - sum(nums)