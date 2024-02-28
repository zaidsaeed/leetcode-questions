class Solution:
    def rob(self, nums: List[int]) -> int:
        res, n = [], len(nums)
        for i in range(n):
            house = nums[i]
            if i == 0:
                res.append(house)
            elif i == 1:
                res.append(max(house, res[0]))
            else:
                option1 = house + res[i-2]
                option2 = res[i-1]
                res.append(max(option1, option2))
        return res[-1]