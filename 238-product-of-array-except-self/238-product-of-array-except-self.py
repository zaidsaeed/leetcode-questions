class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lToR = []
        for i in range(0, len(nums)):
            if i == 0:
                lToR.append(nums[0])
            else:
                lToR.append(lToR[i-1] * nums[i])
        
        rToL = [-1 for i in range(len(nums))]
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                rToL[i] = nums[i]
            else:
                rToL[i] = rToL[i+1] * nums[i]
        
        ans = [-1 for i in range(len(nums))]
        for i in range(len(nums)):
            lProd = 1
            if i - 1 >= 0:
                lProd = lToR[i-1]
            
            rProd = 1
            if i + 1 < len(nums):
                rProd = rToL[i+1]
                
            ans[i] = lProd * rProd
        
        return ans
        
        '''
        nums = [1,2,3,4]
        lR = [1, 2, 6, 24]
        rL = [1,24,12,4]
        '''