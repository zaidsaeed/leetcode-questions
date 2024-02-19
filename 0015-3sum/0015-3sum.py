class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            num1 = nums[i]
            l, r = (i+1), len(nums)-1
            while l < r:
                num2 = nums[l]
                num3 = nums[r]
                target = (num1 * -1)
                if num2 + num3 == target:
                    if r == len(nums) - 1 or (nums[l-1] != nums[l] or nums[r] != nums[r+1]): 
                        ans.append([num1, num2, num3])
                    l += 1
                    r -= 1
                elif num2 + num3 > target:
                    r -= 1
                else:
                    l += 1
        return ans
                    