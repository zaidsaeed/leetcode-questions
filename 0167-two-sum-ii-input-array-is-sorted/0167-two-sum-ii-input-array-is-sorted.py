class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            calcSum = numbers[l] + numbers[r]
            if calcSum == target:
                return [l+1, r+1]
            if calcSum < target:
                l += 1
            else:
                r -= 1
        