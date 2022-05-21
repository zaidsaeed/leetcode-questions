class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def LISRec(index, nums, cache):
            if index in cache:
                return cache[index]
            
            ansArr = [1]
            for i in range(index+1, len(nums)):
                if (nums[i] > nums[index]):
                    ansArr.append(1 + LISRec(i, nums, cache))
                    
            cache[index] = max(ansArr)
            return cache[index]
        
        for i in range(len(nums)):
            LISRec(i, nums, cache)
            
        return max(cache.values())
        
        
        
        '''
        ansArr = [1, 2]
                       [10,9,2,5,3,7,101,18]
                            ind               
                        
                        
            {6: 1, 7:1, 0:2, 1:2, }
        
        '''