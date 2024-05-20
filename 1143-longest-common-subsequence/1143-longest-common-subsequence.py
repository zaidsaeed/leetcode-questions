class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        return self.lcs(text1, text2, 0, 0, memo)
    
    def lcs(self, text1, text2, idx1, idx2, memo):
        if idx1 < len(text1) and idx2 < len(text2):
            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]
            if text1[idx1] == text2[idx2]:
                memo[(idx1, idx2)] = 1 + self.lcs(text1, text2, idx1+1, idx2+1, memo)
                return memo[(idx1, idx2)]
            branch1 = self.lcs(text1, text2, idx1, idx2+1, memo)
            branch2 = self.lcs(text1, text2, idx1+1, idx2, memo)
            memo[(idx1, idx2)] = max(branch1, branch2)
            return memo[(idx1, idx2)]
        return 0

'''
     a b c d e
   a 1 1 1 1 1
   c 1 1 2 2 2 
   e 1 1 2 2 3

'''