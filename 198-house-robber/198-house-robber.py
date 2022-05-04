class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        else:
            ans = [0 for i in range(len(nums))]
            ans[0] = nums[0]
            ans[1] = max(nums[0], nums[1])
            
            for i in range(2, len(nums)):
                ans[i] = max(ans[i-1], ans[i-2] + nums[i])
                
            return ans[-1]
        
    '''
    [103,2,1,3,100]
      ^.   ^.   l
      
      1, 3, 5
      1,4
      
      2,4
      2,5
      
      
      [1,2,3,4]
      1,3
      1,4
      
      2,4
    '''
        