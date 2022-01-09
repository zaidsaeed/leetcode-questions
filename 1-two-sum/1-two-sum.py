class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resMap = {}
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if num in resMap:
                return [resMap[num], i]
            else:
                resMap[diff] = i
            