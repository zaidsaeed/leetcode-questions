class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        nums1 = nums[0:n-1]
        nums2 = nums[1:]
        option1, option2 = self.robArr(nums1), self.robArr(nums2)
        return max(option1, option2)
        
    def robArr(self, nums: List[int]) -> int:
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
    
'''
1,2,3,4,5
'''