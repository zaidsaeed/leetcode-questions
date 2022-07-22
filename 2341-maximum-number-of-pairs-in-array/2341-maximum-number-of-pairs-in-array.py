class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = [0 , 0]
        i = 0
        
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                ans[0] += 1
                i += 2
            else:
                ans[1] += 1
                i += 1
        
        if i < len(nums):
            ans[1] += 1
        
        return ans
    
    '''
        [1, 1, 2, 2, 2, 3]
                        i
    
    '''