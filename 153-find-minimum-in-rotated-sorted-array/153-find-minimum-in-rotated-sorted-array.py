class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            m = l + ((h-l) // 2)
            mid = nums[m]
            if mid < nums[h]:
                h = m
            else:
                l = m + 1
        return nums[l]

# [3,4,5,1,2]
#      l h
#     m
# l move
#
#
# [5,1,2,3,4]
#  l h
#  m
# h move
#
# [1,2,3,4,5]
#  l h    
# h move
#