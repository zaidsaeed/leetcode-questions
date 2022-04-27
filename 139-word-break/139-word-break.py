class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        
        def wordBreakRec(s, wordDict, memo):
            if s in memo:
                return memo[s]
            if len(s) == 0:
                return True

            for word in wordDict:
                end = len(word)
                
                if s[0:end] == word:
                    if wordBreakRec(s[end:], wordDict, memo):
                        memo[s] = True
                        return memo[s]
            memo[s] = False
            return memo[s]
        
        return wordBreakRec(s, wordDict, memo)
        
        print(memo)