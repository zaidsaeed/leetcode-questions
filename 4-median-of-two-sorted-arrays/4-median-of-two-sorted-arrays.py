class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x, y = len(nums1), len(nums2)
        
        if x > y:
            return self.findMedianSortedArrays(nums2, nums1)
        
        l, h = 0, x
        
        halfTotal = (x + y + 1) // 2
        
        while (l <= h):
            partX = l + ((h - l) // 2)
            partY = halfTotal - partX
            
            maxLeftX = float('-inf')
            if partX != 0:
                maxLeftX = nums1[partX -1]
            
            minRightX = float('inf')
            if partX != x:
                minRightX = nums1[partX]
            
            maxLeftY = float('-inf')
            if partY != 0:
                maxLeftY = nums2[partY-1]
            
            minRightY = float('inf')
            if partY != y:
                minRightY = nums2[partY]
                
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                totalLen = x + y
                if totalLen % 2 == 0:
                    a0 = max(maxLeftX, maxLeftY)
                    a1 = min(minRightX, minRightY)
                    return ((a0 + a1) / 2)
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftY >= minRightX:
                l = partX + 1
            else:
                h = partX - 1