class Solution:

    ansMap = {
        1: 1,
        2: 2,
        3: 3
    }
    
    def climbStairs(self, n: int) -> int:
                
        def rec(n):
            if n in Solution.ansMap:
                return Solution.ansMap[n]
            
            ans = rec(n-1) + rec(n-2)
            Solution.ansMap[n] = ans
            return ans
        
        return rec(n)