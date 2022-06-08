class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        minIndex = self.findMinIndex(nums)
        
        print(minIndex)
        
        if target >= nums[minIndex] and target <= nums[-1]:
            ans = self.binSearch(nums[minIndex:] ,target)
            if ans != -1:
                return minIndex + ans
            else:
                return -1
        ans = self.binSearch(nums[0:minIndex] ,target)
        if ans != -1:
            return self.binSearch(nums[0:minIndex] ,target)
        
        return -1
    
    def binSearch(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + ((r-l) // 2)
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                r = mid - 1
        
        return -1
    def findMinIndex(self, nums):
        l, r = 0, len(nums)-1
        minElem = 0
        while l <= r:
            mid = l + ((r-l) // 2)
            minElem = mid
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] == nums[r]:
                break
            else:
                r = mid
        
        return minElem