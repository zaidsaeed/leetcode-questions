class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        dp = [[0]*(p_len+1) for _ in range(s_len+1)]
        
        # dp[0][0] = 1, since empty string matches empty pattern
        dp[0][0] = 1
        # for an empty strings, it is still possible to have a pattern to match it
        # the patter has to be like #*#*#*#*, and all * means empty/0 elems
        for i in range(2, p_len+1):
            if p[i-1]=='*' and dp[0][i-2]:
                dp[0][i] = 1
        
        for i in range(1, s_len+1):
            for j in range(1, p_len+1):
                if (s[i-1]==p[j-1] or p[j-1]=='.'):
                    dp[i][j] = dp[i-1][j-1]
                    
                elif p[j-1]=='*':
                    if p[j-2] != s[i-1] and p[j-2]!='.':       
                        dp[i][j] = dp[i][j-2]
                    else: 
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                        
        return dp[-1][-1]