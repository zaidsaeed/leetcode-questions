class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        numsMap = {}
        
        for num in nums:
            if num in numsMap:
                numsMap[num] = numsMap[num] + 1
            else:
                numsMap[num] = 1
        
        #num of pairs, num of singles
        
        ans = [0, 0]
        
        for val in numsMap.values():
            ans[0] += (val // 2)
            ans[1] += (val % 2)
        
        return ans
    
    
    '''
        [1,3,2,1,3,2,2]
                 ^
        
        map = {1: 2, 2: 3, 3: 2}
        
        ans = [2, 1]
    '''
            