class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0 for i in range(len(height))]
        lMaxVal = height[0]
        for i in range(1, len(leftMax)):
            leftMax[i] = lMaxVal
            lMaxVal = max(lMaxVal, height[i])
        
        
        rightMax = [0 for i in range(len(height))]
        rMaxVal = height[-1]
        for i in range(len(leftMax)-2, -1, -1):
            rightMax[i] = rMaxVal
            rMaxVal = max(rMaxVal, height[i])
        
        ans = 0
        
        for i in range(len(height)):
            add = min(leftMax[i], rightMax[i]) - height[i]
            if add > 0:
                ans += add
        
        
        return ans