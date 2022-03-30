class Solution:
    def maxArea(self, height: List[int]) -> int:
        # More optimal solution
        lInd, rInd = 0, (len(height) - 1)
        ans = float('-inf')
        while rInd > lInd:
            areaCalculated = min(height[lInd], height[rInd]) * (rInd - lInd)
            ans = max(ans, areaCalculated)
            if height[rInd] > height[lInd]:
                lInd += 1
            else:
                rInd -= 1
        return ans
        
        #O(n^2 solution)
        # have two pointers one iterates from beg. to 2 pointer
        # move rightmost pointer one to the left after each iteration
        # keep track of max
        # rPointer = len(height) - 1
        # ans = float('-inf')
        # while (rPointer > 0):
        #     for lPointer in range(rPointer):
        #         ans = max(ans, ((rPointer - lPointer) * min(height[rPointer], height[lPointer])))
        #     rPointer -= 1
        # return ans
                
            
        
        