class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def findMin(nums):
            l, h = 0, len(nums) - 1
            while l < h:
                m = l + ((h-l) // 2)
                mid = nums[m]
                if mid > nums[h]:
                    l = m + 1
                else:
                    h = m
            return l
        
        def binSearch(arr, target):
            l, h = 0, len(arr) - 1
            while l <= h:
                m = l + ((h-l) // 2)
                mid = arr[m]
                if mid == target:
                    return m
                elif mid > target:
                    h = m - 1
                else:
                    l = m + 1
            return -1
        
        minIndex = findMin(nums)
        arr = None
        if (target > nums[-1]):
            arr = nums[:minIndex]
            return binSearch(arr, target)
        else:
            arr = nums[minIndex:]
            ans = binSearch(arr, target) 
            if ans != -1:
                return minIndex + binSearch(arr, target)
            return -1