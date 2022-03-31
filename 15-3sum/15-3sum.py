class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(0, len(nums)):
            numI = nums[i]
            j = i + 1
            k = len(nums) - 1
            while (j < k):
                numJ = nums[j]
                numK = nums[k]
                currSum = numI + numJ + numK
                if currSum < 0:
                    j += 1
                elif currSum > 0:
                    k -= 1
                else:
                    ans.add((numI, numJ, numK))
                    j += 1
                    k -= 1
        return ans

    
    ## [-1,0,1,2,-1,-4]
    ##[-4, -1, -1, 0, 1, 2]
                      # i  j  k