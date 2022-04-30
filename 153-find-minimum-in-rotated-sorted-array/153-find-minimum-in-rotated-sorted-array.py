class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h= 0, len(nums) -1
        while l < h:
            mid = (h+l) // 2
            if nums[h] > nums[mid]:
                h = mid
            else:
                l = mid + 1
        
        return nums[l]
    
    
    '''
    [4,5,1,2,3]
         lh   
    '''