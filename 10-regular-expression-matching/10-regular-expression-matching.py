class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        dp = [[0]*(p_len+1) for _ in range(s_len+1)]
        
        # dp[0][0] = 1, since empty string matches empty pattern
        dp[0][0] = 1
        
        #firstt row only
        for j in range(1, p_len):
            if p[j] == '*':
                dp[0][j+1] = dp[0][j-1]
        
        for i in range(1, s_len+1):
            for j in range(1, p_len+1):
                first_match = p[j-1] in {s[i-1], '.'}
                if first_match:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if dp[i][j-2]:
                        dp[i][j] = 1
                    elif s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] = dp[i-1][j]
        
        print(dp)
        return dp[-1][-1]
    
    
    
    '''
    
    
                a *
              t f f
            a f t 
            a f
                x a * b . c
              t f f f f f f
            x f
            a f
            a f
            b f
            y f
            c f
    
    
    
    
    '''