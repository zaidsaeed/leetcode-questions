class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(heights)
        for i in range(len(heights)-1, -1, -1):
            curr_height = heights[i]
            cnt = 0
            while stack and curr_height > stack[-1]:
                stack.pop()
                ans[i] += 1 
            if stack:
                ans[i] += 1
            stack.append(curr_height)
        return ans
            