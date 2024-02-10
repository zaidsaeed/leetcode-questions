class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans, l, r = 0, 0, len(height) - 1
        while l < r:
            lPole, rPole = height[l], height[r]
            ans = max(ans, (min(lPole, rPole) * (r-l)))
            if lPole > rPole:
                r -= 1
            else:
                l += 1
        return ans