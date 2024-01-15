class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seenSet = set()
        for i in range(len(nums)):
            num = nums[i]
            if num in seenSet:
                return True
            seenSet.add(num)
        return False
        