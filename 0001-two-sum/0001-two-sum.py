class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = self.createNumsDict(nums)
        for i in range(len(nums)):
            num = nums[i]
            if (target - num) in numsDict and i != numsDict[target - num]:
                ans = []
                ans.append(i)
                ans.append(numsDict[target - num])
                return ans
    
    def createNumsDict(self, nums):
        numsDict = {}
        for i in range(len(nums)):
            numsDict[nums[i]] = i
        return numsDict
    
    
    '''
    [2,7,11,15]
    numsDict =
    {
        2: 0,
        7: 1,
        11: 2,
        15: 3
    }
    target=9
    '''